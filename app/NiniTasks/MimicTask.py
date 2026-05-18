from crewai import Task
from app.agents.MimicAgent import MimicAgent

MimicAgentTask= Task(
    description="Consumir dados do dataset MIMIC",
    expected_output="Gerar {diagnosticoMimic} médico com base nos registros do dataset",
    agent= MimicAgent,
    context=[NiniTaskTriage]
)