from crewai import Task
from app.agents.Judge import Judge

JudgeTask=Task(
    description="Consumir o {diagnosticoPub} e o {diagnosticoMimic}.",
    expected_output="com base no {diagnosticoPub}, e {diagnosticoMimic}, gerar,analisar e fornecer o {diagnosticoFinal}",
    agent= Judge,
    context= [NiniTaskTriage,MimicAgentTask,PubMedTask]
)