from crewai import Task
<<<<<<< HEAD
from app.agents.Judge import Juiz
from app.NiniTasks.MimicTask import MimicAgentTask
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage
from app.NiniTasks.PubTask import PubMedTask

JudgeTask=Task(
    description="Consumir o diagnostico Pub e o diagnosticoMimic.",
    expected_output="com base no diagnóstico Pub, e diagnostico Mimic, gerar,analisar e fornecer o diagnostico Final",
    agent= Juiz,
    context= [NiniTaskTriage,MimicAgentTask,PubMedTask]
=======
from app.agents.judge import judge

judgetask=Task(
    description="analisar o {diagnosticomimic} e o {diagnosticopub} para dar o veredito final em {diagnosticofinal}",
    context="use o output de {diagnosticomimic} e {diagnosticopub} para gerar o {diagnosticofinal}",
    expected_output = "diagnostico consolidado em {diagnosticofinal}",
    agent=judge

>>>>>>> d5104b514895dc2362c621e68711e7e7d4f2eb4e
)