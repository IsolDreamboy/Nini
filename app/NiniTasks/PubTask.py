from crewai import Task
from app.agents.PubAgent import PubAgent
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage

PubMedTask=Task(
    description="Consumir dados do dataset PubMed",
    expected_output="Gerar diagnóstico com base nos relatorios do dataset.",
    agent=PubAgent,
    context = [NiniTaskTriage]
)