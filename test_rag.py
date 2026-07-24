from src.knowledge.search import search
from src.knowledge.prompt_builder import generate_prompt
from src.llm.client import ask_llm


def main():

    question = input("Pergunta: ")

    results = search(question)

    prompt = generate_prompt(question, results)

    print("\n")
    print("=" * 60)
    print("PROMPT")
    print("=" * 60)
    print(prompt)

    print("\n")
    print("=" * 60)
    print("RESPOSTA")
    print("=" * 60)

    answer = ask_llm(prompt)

    print(answer)


if __name__ == "__main__":
    main()