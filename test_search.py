from src.knowledge.search import search

results = search("Minha entrega está demorando.")

def generate_prompt(question, results):

    prompt = """
Você é um assistente da TechStore.

Responda apenas utilizando as informações abaixo.

Se a resposta não estiver no contexto, informe isso ao usuário.

CONTEXTO:

"""

    for filename, chunk, distance in results:

        prompt += f"""
Documento: {filename}

{chunk}

-------------------------

"""

    prompt += f"""

PERGUNTA:

{question}

RESPOSTA:
"""

    return prompt