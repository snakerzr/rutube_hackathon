from itertools import zip_longest

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase
from deepeval.test_case import LLMTestCaseParams
from deepeval.dataset import EvaluationDataset

from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

# TODO:
# Что то придумать с сохранением результатов оценки

OPENAI_MODEL = 'gpt-4o-mini'

def create_deepeval_dataset(
    user_queries: list[str], 
    actual_outputs: list[str], 
    expected_outputs: list[str] | None = None, 
    expected_contexts: list[list[str]] | None = None, 
    actual_contexts: list[list[str]] | None = None
) -> EvaluationDataset:
    
    # Проверка длины обязательных списков
    if len(actual_outputs) != len(user_queries):
        raise ValueError(f"Length mismatch: 'actual_outputs' has {len(actual_outputs)} items, "
                         f"but 'user_queries' has {len(user_queries)}.")
    
    # Проверка длины необязательных списков
    if expected_outputs and len(expected_outputs) != len(user_queries):
        raise ValueError(f"Length mismatch: 'expected_outputs' has {len(expected_outputs)} items, "
                         f"but 'user_queries' has {len(user_queries)}.")
    
    if expected_contexts and len(expected_contexts) != len(user_queries):
        raise ValueError(f"Length mismatch: 'expected_contexts' has {len(expected_contexts)} items, "
                         f"but 'user_queries' has {len(user_queries)}.")
    
    if actual_contexts and len(actual_contexts) != len(user_queries):
        raise ValueError(f"Length mismatch: 'actual_contexts' has {len(actual_contexts)} items, "
                         f"but 'user_queries' has {len(user_queries)}.")
    
    # Создание тест-кейсов
    test_cases = []

    for query, actual_output, expected_output, expected_context, actual_context in zip_longest(
        user_queries, 
        actual_outputs, 
        expected_outputs or [], 
        expected_contexts or [], 
        actual_contexts or []
    ):
        test_case_kwargs = {
            'input': query,
            'actual_output': actual_output,
            **({'expected_output': expected_output} if expected_output else {}),
            **({'context': expected_context} if expected_context else {}),
            **({'retrieval_context': actual_context} if actual_context else {})
        }

        test_cases.append(LLMTestCase(**test_case_kwargs))
    
    return EvaluationDataset(test_cases=test_cases)

# NOTE: Метрики
# 1. Документы релевантны вопросу?
# 2. Отвечает ли ответ на вопрос?
# 3. Галлюцинации: ответ основан на найденных документах?

relevance_metric = GEval(
    model=OPENAI_MODEL,
    name="Document Relevance",
    strict_mode=True,  # Enforce strict binary scoring
    evaluation_steps=[
        "Check if the 'retrieval_context' contains documents that are directly relevant to the 'input'. Penalize if the documents are not related to the user's question.",
        "Verify that key terms or concepts from the 'input' are represented in the 'retrieval_context'. Heavily penalize if any critical information is missing.",
        "Ensure that the 'retrieval_context' covers all necessary facts or details to fully answer the 'input'. Penalize for omissions of important information.",
        "Allow for minor irrelevant content in the 'retrieval_context', but penalize if it significantly distracts from the relevance to the 'input'."
    ],
    evaluation_params=[
        LLMTestCaseParams.INPUT,  # The user's question or query
        LLMTestCaseParams.RETRIEVAL_CONTEXT  # The retrieved documents to check for relevance
    ]
)

answer_relevance_metric = GEval(
    model=OPENAI_MODEL,
    name="Answer Relevance and Completeness",
    strict_mode=True,  # Enforce strict binary scoring
    evaluation_steps=[
        "Check if the 'actual_output' directly addresses the main point(s) of the 'input'. Penalize if the answer is off-topic or misses the core question.",
        "Verify whether the facts in the 'actual_output' align with the 'input' and any provided context. Penalize if any factual contradictions are present.",
        "Heavily penalize omission of critical details from the 'actual_output'. Ensure that all relevant parts of the 'input' are addressed.",
        "Minor vagueness or unnecessary information can be tolerated, but penalize if it confuses the user or detracts from the clarity of the response."
    ],
    evaluation_params=[
        LLMTestCaseParams.INPUT,  # The user's question or query
        LLMTestCaseParams.ACTUAL_OUTPUT  # The generated answer to evaluate
    ]
)

hallucination_detection_metric = GEval(
    model=OPENAI_MODEL,
    name="Hallucination Detection",
    strict_mode=True, 
    evaluation_steps=[
        "Check if all factual information in the 'actual_output' is grounded in the 'retrieval_context'. Penalize if any information is introduced that is not supported by the retrieved documents.",
        "Heavily penalize if key facts in the 'actual_output' are fabricated or not present in the 'retrieval_context'.",
        "Ensure that the 'actual_output' accurately reflects the information in the 'retrieval_context'. Slight vagueness or subjectivity is allowed if it does not introduce new or false facts.",
        "Minor omissions from the 'retrieval_context' can be tolerated, but the answer should not rely on unsupported or external information."
    ],
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,  # The model's generated answer
        LLMTestCaseParams.RETRIEVAL_CONTEXT  # The documents used to generate the answer
    ]
)

correctness_metric = GEval(
    model=OPENAI_MODEL,
    name="Correctness",
    criteria="Determine whether the actual output is factually correct based on the expected output.",
    strict_mode=True,
    # NOTE: you can only provide either criteria or evaluation_steps, and not both
    evaluation_steps=[
        "Check whether the facts in 'actual output' contradicts any facts in 'expected output'",
        "You should also heavily penalize omission of detail",
        "Vague language, or contradicting OPINIONS, are OK"
    ],
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
)

def g_evaluate(
    user_queries: list[str], 
    actual_outputs: list[str], 
    expected_outputs: list[str] | None = None, 
    expected_contexts: list[list[str]] | None = None, 
    actual_contexts: list[list[str]] | None = None
) -> EvaluationDataset:
    dataset = create_deepeval_dataset(
        user_queries=user_queries,
        actual_outputs=actual_outputs,
        expected_outputs=expected_outputs,
        actual_contexts=retrieval_contexts
    )

    # Evaluate the dataset using the defined metrics
    dataset.evaluate([relevance_metric, answer_relevance_metric, hallucination_detection_metric, correctness_metric])

    return dataset
    

if __name__ == '__main__':
    # Define test data
    user_queries = [
        "What are the causes of climate change?",
        "Who was the first person to step on the moon?",
        "Who wrote the play Hamlet?"
    ]

    actual_outputs = [
        "Climate change is caused by greenhouse gases like CO2.",
        "Neil Armstrong was the first person to step on the moon on July 20, 1969.",
        "Hamlet was written by William Shakespeare and performed for the first time in 1500."
    ]

    # Since these are expected outputs, when not relevant, we can use empty strings
    expected_outputs = [
        "This is an example",  # Not relevant for hallucination or answer relevance in the first case
        "Neil Armstrong was the first person to step on the moon.",
        None  # Not used in the hallucination detection case
    ]

    # For retrieval contexts, use empty lists instead of None when there's no context required
    retrieval_contexts = [
        ["Climate change is a long-term change in the average weather patterns that define Earth’s local, regional, and global climates."],  # Relevant for Document Relevance
        [''],  # Not used for answer relevancy or relevance in this case
        ["Hamlet, a tragedy written by William Shakespeare, is believed to have been first performed in 1609."]  # Relevant for Hallucination Detection
    ]
    g_evaluate(
        user_queries=user_queries,
        actual_outputs=actual_outputs,
        expected_outputs=expected_outputs,
        actual_contexts=retrieval_contexts
    )