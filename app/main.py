import os
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "Nini"}

@app.get("/teste/{teste_id}")
def read_teste(teste_id: int, q: str | None = None):
  return {"teste_id": teste_id, "q": q}

@app.post("/tst")
def read_tst(tst_id : int, q:str | None = None):
  return{"tst_id": teste_id, "q": q}