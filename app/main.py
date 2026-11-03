from fastapi import FastAPI
from app.api.v1.triage import router as triage_router
from fastapi.middleware.cors import CORSMiddleware
from app.db import models
from app.db.connection import engine, Base

Base.metadata.create_all(bind=engine)

app= FastAPI(
  title="Nini",
  description="API para triagem",
  version="1.0.0"
)

#Middleware para permitir requisições de qualquer origem (CORS)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(triage_router, prefix="/api/v1")

@app.get("/health")
def health_check():
  return {"status": "operational","system": "Nini"}