from crewai import Agent
from app.config.settings import settings

Judge=Agent(
    role="",
    backstory="".
    goal="",
    llm = settings.MODEL_PRO,
    allow_dellegation= True
)