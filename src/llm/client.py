import ollama

from src.config import OLLAMA_MODEL


def ask_llm(prompt: str) -> str:
    """
    Envia um prompt para o Ollama e retorna a resposta.
    """

    try:

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente da TechStore. "
                        "Responda apenas utilizando o contexto fornecido."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response["message"]["content"]

    except Exception as e:

        raise RuntimeError(
            f"Erro ao comunicar com o Ollama: {e}"
        )