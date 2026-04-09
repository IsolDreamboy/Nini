from crewai import Agent
from app.config.settings import settings

apub=Agent(
   role="",
   goal="",
   backstory="",
   llm= settings.MODEL_PRO,
   allow_delegation=False
)