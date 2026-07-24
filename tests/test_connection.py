from src.database.connection import get_connection

try:
    conn = get_connection()

    print("✅ Conexão realizada com sucesso!")

    conn.close()

except Exception as e:
    print(e)