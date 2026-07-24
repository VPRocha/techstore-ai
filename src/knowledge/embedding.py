from sentence_transformers import SentenceTransformer

from src.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embedding(text: str):
    """
    Gera um embedding para um texto.
    """

    return model.encode(text)