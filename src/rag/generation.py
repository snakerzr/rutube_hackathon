import requests

from config import OLLAMA_ENDPOINT
from templates import FILTERING_TEMPLATE, QUERY_REWRITING_PROMPT_TEMPLATE


def generate(prompt: str, temperature: float = 0, return_str_only: bool = True) -> dict:
    result = requests.post(
        OLLAMA_ENDPOINT,
        json={
            "model": "mistral-nemo",
            "options": {"seed": 123, "temperature": temperature},
            "prompt": prompt,
            "stream": False,
        },
    ).json()
    if return_str_only:
        return result["response"]
    else:
        return result


def chunk_filtering(query: str, context: str) -> bool:
    response = generate(FILTERING_TEMPLATE.format(query=query, context=context))
    if "0" in response[:10]:
        return False
    elif "1" in response[:10]:
        return True


def rewrite_query(user_input):
    response = generate(QUERY_REWRITING_PROMPT_TEMPLATE.format(query=user_input))
    return response
