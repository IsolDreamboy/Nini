from crewai import Task
from app.agents.MimicAgent import MimicAgent
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage

MimicAgentTask= Task(
    description="Consumir dados do dataset MIMIC",
    expected_output="Gerar diagnostico Mimic médico com base nos registros do dataset",
    agent= MimicAgent,
    context=[NiniTaskTriage]
)