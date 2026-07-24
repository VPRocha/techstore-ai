from src.database.connection import get_connection
from src.knowledge.embedding import generate_embedding


def search(query: str):

    embedding = generate_embedding(query)

    vector = "[" + ",".join(map(str, embedding.tolist())) + "]"

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        SELECT
            filename,
            chunk,
            embedding <=> %s::vector AS distance
        FROM knowledge_base
        ORDER BY distance
        LIMIT 3;
    """

    cursor.execute(sql, (vector,))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results