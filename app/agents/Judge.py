from crewai import Agent
from app.config.settings import settings

Judge=Agent(
    role="Juiz",
    backstory="Você é o juiz, analisa os diagnosticos, absorve o que é viavel, e gera o diagnostico final. ".
    goal="analisar o {diagnosticoMimic} e {diagnosticoPub} para  gerar o {diagnosticoFinal}",
    llm = settings.MODEL_PRO,
    allow_dellegation= True
)