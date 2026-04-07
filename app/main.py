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
        'pergunta': 'Nini, eu não sei o que está acontecendo... comecei a sentir fraqueza nas pernas, caí duas vezes essa semana e agora parece que meus músculos estão pulando sozinhos debaixo da pele. O médico mencionou Esclerose Lateral Amiotrófica e eu perdi o chão. O que eu faço?',
        'contexto': """Área da saúde"""
      }

      resultado = nini_app.crew().kickoff(inputs=inputs)
      
      print(resultado)

    except Exception as e:
      print(f"Erro ao executar o Nini: {str(e)}")

if __name__=="__main__":
    run_nini()

