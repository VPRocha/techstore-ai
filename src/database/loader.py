from psycopg import sql

from src.database.connection import get_connection
from src.utils.logger import logger


def load_dataframe(df, table_name, columns):
    """
    Carrega um DataFrame para uma tabela do PostgreSQL.
    """

    df = df.where(df.notna(), None)

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        placeholders = ", ".join(["%s"] * len(columns))

        query = sql.SQL("""
            INSERT INTO {} ({})
            VALUES ({})
            ON CONFLICT DO NOTHING
        """).format(
            sql.Identifier(table_name),
            sql.SQL(", ").join(map(sql.Identifier, columns)),
            sql.SQL(placeholders),
        )

        data = df[columns].values.tolist()

        cursor.executemany(query, data)

        conn.commit()

        logger.info(
            f"{len(data)} registros carregados para '{table_name}'."
        )

    except Exception as e:

        if conn:
            conn.rollback()

        logger.exception(f"Erro ao carregar '{table_name}': {e}")
        raise

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()