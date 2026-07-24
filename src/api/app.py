from fastapi import FastAPI

from src.api.routes import router


app = FastAPI(
    title="TechStore AI",
    description="API RAG para atendimento ao cliente da TechStore",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "TechStore AI está funcionando!"
    }