from crewai import Agent
from app.config.settings import settings

judge=Agent(
    role="Juiz validador",
    goal="Consolidar dados e validar em {diagnosticofinal}",
    backstory="",
    llm=settings.MODEL_PRO,
    allow_delegation=True
)