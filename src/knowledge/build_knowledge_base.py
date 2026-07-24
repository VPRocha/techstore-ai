from src.knowledge.loader import load_documents
from src.knowledge.chunker import chunk_text
from src.knowledge.embedding import generate_embedding

from src.database.knowledge_loader import insert_chunk


def main():

    print("=" * 50)
    print("Construindo Knowledge Base...")
    print("=" * 50)

    documents = load_documents()

    for document in documents:

        filename = document["filename"]
        content = document["content"]

        chunks = chunk_text(content)

        print(f"{filename}: {len(chunks)} chunks")

        for chunk in chunks:

            embedding = generate_embedding(chunk)

            insert_chunk(
                filename,
                chunk,
                embedding
            )

    print("=" * 50)
    print("Knowledge Base criada com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()