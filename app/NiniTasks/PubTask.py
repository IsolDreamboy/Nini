from crewai import Task
from app.agents.PubAgent import PubAgent

PubMedTask=Task(
    description="Consumir dados do dataset PubMed",
    expected_output="Gerar {diagnosticoPub} com base nos relatorios do dataset.",
    agent=PubAgent,
    context = [NiniTaskTriage]
)