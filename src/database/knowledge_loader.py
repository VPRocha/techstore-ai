from psycopg import sql

from src.database.connection import get_connection


def insert_chunk(filename, chunk, embedding):
    """
    Insere um chunk e seu embedding na knowledge_base.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = sql.SQL("""
        INSERT INTO knowledge_base
        (filename, chunk, embedding)
        VALUES (%s, %s, %s)
        ON CONFLICT (filename, chunk)
        DO NOTHING
    """)

    cursor.execute(
        query,
        (
            filename,
            chunk,
            embedding.tolist()
        )
    )

    conn.commit()

    cursor.close()
    conn.close()