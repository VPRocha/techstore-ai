from sentence_transformers import SentenceTransformer

# Carrega o modelo apenas uma vez
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def generate_embedding(text: str):
    """
    Gera um embedding para um texto.
    """

    return model.encode(text)