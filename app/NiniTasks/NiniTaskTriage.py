from app.agents.Nini import Nini
from crewai import Task


NiniTaskTriage = Task(
    description="""Você vai responder a {pergunta} de maneira gentil e educada, como se tivesse acolhendo a pessoa que pergunta como se fosse um amigo, fale de maneira descontraída.""",
    expected_output="uma resposta fofa e amavel",
    agent= Nini

)