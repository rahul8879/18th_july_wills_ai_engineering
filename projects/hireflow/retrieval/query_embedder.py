from typing import List
from openai import OpenAI
from config import settings

_client = None
def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=settings.openai_api_key)
    return _client


def embed_query(text: str) -> List[float]:
    """
    Embed a query using OpenAI's embedding model.

    Args:
        text (str): The text to be embedded.

    Returns:
        List[float]: The embedding vector for the input text.
    """
    client = _get_client()
    response = client.embeddings.create(
        model=settings.openai_embedding_model,
        input=text
    )
    return response.data[0].embedding