from crewai import Task
from app.agents.amimic import amimic

amimictask=Task(
    description="analise o {relatoriopaciente} para consumir o banco de dados e fornecer o {diagnosticomimic}",
    context="use os dados de {relatoriopaciente} para gerar o {diagnosticomimic}",
    expected_output="{diagnosticomimic}",
    agent=amimic
)