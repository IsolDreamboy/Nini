from crewai import Agent
from app.config.settings import settings

PubAgent=Agent(
    role="",
    backstory="",
    goal="",
    llm= settings.MODEL_PRO,
    allow_dellegation= True
)