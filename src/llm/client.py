import ollama


def ask_llm(prompt: str) -> str:
    """
    Envia um prompt para o Ollama e retorna a resposta do modelo.
    """

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente da TechStore. "
                    "Responda apenas utilizando as informações fornecidas no contexto. "
                    "Se a resposta não estiver no contexto, informe isso ao usuário."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]