from crewai import Agent
from app.config.settings import settings

PubAgent=Agent(
    role="Agente PubMed",
    backstory="Você é um agente que consome os dados do dataset PubMed, e usa os relatorios/dados para gerar o diagnosticoMimic",
    goal="consumir o dataset mimic e gerar o {diagnosticoMimic}",
    llm= settings.MODEL_PRO,
    allow_dellegation= True
)