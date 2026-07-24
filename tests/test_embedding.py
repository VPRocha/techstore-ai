from sklearn.metrics.pairwise import cosine_similarity

from src.knowledge.embedding import generate_embedding

texto1 = "Meu pedido atrasou."
texto2 = "Minha entrega está demorando."
texto3 = "Como alterar minha senha?"

emb1 = generate_embedding(texto1)
emb2 = generate_embedding(texto2)
emb3 = generate_embedding(texto3)

print(
    cosine_similarity([emb1], [emb2])
)

print(
    cosine_similarity([emb1], [emb3])
)