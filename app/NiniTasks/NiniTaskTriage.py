from app.agents.Nini import Nini
from crewai import Task


NiniTaskTriage = Task(
    description="""Você vai coletar os dados do paciente para gerar o relatorio do mesmo, para ser consumido pelos outros agentes""",
    expected_output="Gerar um relatorio paciente, que será usado como base para os diagnosticos iniciais.",
    agent= Nini

)