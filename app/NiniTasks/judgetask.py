from crewai import Task
from app.agents.Judge import Juiz
from app.NiniTasks.MimicTask import MimicAgentTask
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage
from app.NiniTasks.PubTask import PubMedTask

JudgeTask=Task(
    description="Consumir o diagnostico Pub e o diagnosticoMimic.",
    expected_output="com base no diagnóstico Pub, e diagnostico Mimic, gerar,analisar e fornecer o diagnostico Final",
    agent= Juiz,
    context= [NiniTaskTriage,MimicAgentTask,PubMedTask]
)