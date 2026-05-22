import os
from dotenv import load_dotenv
from app.crew import NiniCrew
from app.config.settings import settings

load_dotenv()

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

