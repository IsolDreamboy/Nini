from crewai import Agent
from app.config.settings import settings

PubAgent=Agent(
    role="Agente PubMed",
    backstory="Você é um agente que consome os dados do dataset PubMed, e usa os relatorios/dados para gerar o diagnóstico Mimic",
    goal="consumir o dataset mimic e gerar o diagnóstico mimic",
    llm= settings.MODEL_PRO,
    allow_dellegation= True
)