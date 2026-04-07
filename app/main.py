import os
from dotenv import load_dotenv
from app.agents.Nini import Nini

load_dotenv()

def run_nini():
    print("Teste um, amo minha esposa")
    
    try:
      nini_instance = Nini()

      inputs={
        'pergunta': 'Explique por que eu amo minha esposa'
        'contexto': 'Relacionamentos muito amorosos, que parecem ser de outras vidas(se essas existirem)'
      }

      resultado = nini_instance.crew().kickoff(inputs=inputs)
      print("\n Claro, aqui está sua resposta!")
      print(resultado)

    except Exception as e:
      print(f"Erro ao executar o Nini: {str(e)}")

if __name__=="__main__":
    run_nini()

