from crewai import Task
from app.agents.judge import judge

judgetask=Task(
    description="analisar o {diagnosticomimic} e o {diagnosticopub} para dar o veredito final em {diagnosticofinal}",
    context="use o output de {diagnosticomimic} e {diagnosticopub} para gerar o {diagnosticofinal}",
    expected_output = "diagnostico consolidado em {diagnosticofinal}",
    agent=judge

)