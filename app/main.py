from fastapi import FastAPI
from app.api.v1.triage import router as triage_router

app= FastAPI(
  title="Nini",
  description="API para triagem",
  version="1.0.0"
)

app.include_router(triage_router)

@app.get("/health")
def health_check():
  return {"status": "operational","system": "Nini"}