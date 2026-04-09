from crewai import Task
from app.agents.apub import apub

apubtask=Task(
  description="consumir banco de dados para fornecer o {diagnosticopub}",
  context="analisar sintomas e dados com base no {relatoriopaciente} e dar diagnostico para o paciente conforme os dados consumidos",
  expected_output="diagnostico {diagnosticopub} com referencias para passar pro juiz.",
  agent= apub
 )