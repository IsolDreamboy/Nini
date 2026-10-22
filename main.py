<<<<<<< HEAD
import os
from fastapi import FastAPI

app=FastAPI()

<<<<<<<< HEAD:main.py
def run_nini():
    print("amo minha esposa")
    
    try:
      nini_app = NiniCrew()

      inputs={
        'dadosPaciente': 'ansia de vomito, tontura, pressao alta, depressao',
        
      }

      resultado = nini_app.crew().kickoff(inputs=inputs)
      
      print(resultado)

    except Exception as e:
      print(f"Erro ao executar o Nini: {str(e)}")

if __name__=="__main__":
    run_nini()
========
@app.get("/")
def read_root():
  return {"Hello": "Nini"}
>>>>>>>> d5104b5 (Alterações cruciais):app/main.py

@app.get("/item/{item_id}")
def read_item(item_id: int, q: str | None = None):
  return {"item_id": item_id, "q": q}
=======
def main():
    print("Hello from nini!")


if __name__ == "__main__":
    main()
>>>>>>> d5104b5 (Alterações cruciais)
