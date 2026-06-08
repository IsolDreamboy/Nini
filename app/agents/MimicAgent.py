from crewai import Agent
from app.config.settings import settings
 

MimicAgent=Agent(
    role="Agente Mimic",
    backstory="Você é um agente que consome o dataset e com base em dados/relatorios, você gera um diagnostico",
    goal="consumir o dataset do mimic para gerar o diagnostico Mimic",
    llm= settings.MODEL_GROQ,
    allow_dellegation = True
)