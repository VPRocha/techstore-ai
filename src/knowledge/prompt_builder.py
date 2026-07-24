def generate_prompt(question: str, results) -> str:
    """
    Monta o prompt que será enviado ao LLM.
    """

    prompt = """
Você é um assistente da TechStore.

Responda apenas utilizando as informações do CONTEXTO.

Se a resposta não estiver no contexto, informe isso ao usuário.

========================
CONTEXTO
========================

"""

    for filename, chunk, distance in results:

        prompt += f"""
Documento: {filename}

{chunk}

----------------------------------------

"""

    prompt += f"""

========================
PERGUNTA
========================

{question}

========================
RESPOSTA
========================

"""

    return prompt