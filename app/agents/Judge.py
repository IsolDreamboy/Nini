from crewai import Agent
from app.config.settings import settings

Juiz=Agent(
    role="Juiz",
    backstory="Você é o juiz, analisa os diagnosticos, absorve o que é viavel, e gera o diagnostico final. ",
    goal="analisar o diagnóstico do mimic e diagnóstico Pub para  gerar o diagnóstico final",
    llm = settings.MODEL_PRO,
    allow_dellegation= True
)