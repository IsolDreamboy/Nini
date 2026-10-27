from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from app.api.v1.triage import router as triage_router

app = FastAPI(
    title="Nini Triage API",
    description="Motor de triagem médica e orquestração de agentes",
    version="1.0.0"
)

app.include_router(triage_router)

@app.get("/health")
def health_check():
    return {"status": "operational", "system": "Nini"}