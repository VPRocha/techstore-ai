from pathlib import Path

KNOWLEDGE_BASE = Path("knowledge_base")


def load_documents():
    """
    Lê todos os arquivos .md da base de conhecimento.
    """

    documents = []

    for file in KNOWLEDGE_BASE.glob("*.md"):

        with open(file, "r", encoding="utf-8") as f:

            documents.append(
                {
                    "filename": file.name,
                    "content": f.read()
                }
            )

    return documents