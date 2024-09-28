from chromadb import Collection

from rag.generation import chunk_filtering, generate, rewrite_query
from rag.retriever import (
    classify,
    extract_context_for_generation,
    format_retrieve_result,
    retrieve_relevant_chunks,
)
from templates import PROMPT_TEMPLATE


def rag_pipeline(input: str, collection: Collection) -> dict:
    actual_context_raw = retrieve_relevant_chunks(
        collection=collection, query=input, n_results=5
    )
    actual_context = format_retrieve_result(actual_context_raw)
    actual_context_to_llm = extract_context_for_generation(actual_context)
    prompt = PROMPT_TEMPLATE.format(query=input, context=actual_context_to_llm)
    response = generate(prompt)

    result = {
        "input": input,
        "actual_context": actual_context,
        "actual_response": response,
    }

    return result


def rag_pipeline_with_llm_filtering(input: str, collection: Collection) -> dict:
    actual_context_raw = retrieve_relevant_chunks(
        collection=collection, query=input, n_results=10
    )
    actual_context = format_retrieve_result(actual_context_raw)

    context_llm_filtered = []
    for cont in actual_context[0]:
        if chunk_filtering(input, extract_context_for_generation([[cont]])):
            context_llm_filtered.append(cont)

    context_llm_filtered = [context_llm_filtered]

    actual_context_to_llm = extract_context_for_generation(context_llm_filtered)
    prompt = PROMPT_TEMPLATE.format(query=input, context=actual_context_to_llm)
    response = generate(prompt)

    result = {
        "input": input,
        "actual_context": actual_context,
        "actual_response": response,
    }

    return result


def rag_pipeline_with_classification_filtering(
    input: str, collection: Collection
) -> dict:
    class_1 = classify(input)[0]

    actual_context_raw = retrieve_relevant_chunks(
        collection=collection, query=input, n_results=10, where={"class_1": class_1}
    )
    actual_context = format_retrieve_result(actual_context_raw)

    actual_context_to_llm = extract_context_for_generation(actual_context)
    prompt = PROMPT_TEMPLATE.format(query=input, context=actual_context_to_llm)
    response = generate(prompt)

    result = {
        "input": input,
        "actual_context": actual_context,
        "actual_response": response,
    }

    return result


def rag_pipeline_with_query_rewriting(input: str, collection: Collection) -> dict:
    rewrited_input = rewrite_query(input)
    actual_context_raw = retrieve_relevant_chunks(
        collection=collection, query=rewrited_input, n_results=5
    )
    actual_context = format_retrieve_result(actual_context_raw)
    actual_context_to_llm = extract_context_for_generation(actual_context)
    prompt = PROMPT_TEMPLATE.format(query=input, context=actual_context_to_llm)
    response = generate(prompt)

    result = {
        "input": input,
        "actual_context": actual_context,
        "actual_response": response,
    }

    return result
