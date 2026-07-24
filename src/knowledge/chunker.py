def chunk_text(text, chunk_size=300):
    """
    Divide um texto em pedaços menores.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks