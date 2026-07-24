from src.knowledge.loader import load_documents
from src.knowledge.chunker import chunk_text

docs = load_documents()

for doc in docs:

    print("=" * 50)
    print(doc["filename"])

    chunks = chunk_text(doc["content"])

    print(f"Total de chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {i}")
        print(chunk)