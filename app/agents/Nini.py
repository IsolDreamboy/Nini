from crewai import Agent
from app.config import settings

Nini=Agent(
    role="Você é Nini",
    goal="Coletar dados dos pacientes e armazena-los",
    backstory="",
    llm= settings.MODEL_FLASH,
    allow_dellegation=True
)