CREATE TABLE IF NOT EXISTS knowledge_base (

    id SERIAL PRIMARY KEY,

    filename TEXT NOT NULL,

    chunk TEXT NOT NULL,

    embedding VECTOR(384)

);