from src.knowledge.search import search
from src.knowledge.prompt_builder import generate_prompt
from src.llm.client import ask_llm


def chat(question: str) -> str:
    """
    Executa todo o pipeline RAG.
    """

    results = search(question)

    prompt = generate_prompt(question, results)

    answer = ask_llm(prompt)

    return answer