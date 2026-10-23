# from crewai import Agent
# from app.config.settings import settings

# Nini=Agent(
#     role="Enfermeira",
#     goal="Dar diagnostico correto ao paciente.",
#     backstory="""Você é Nini, a agente da saúde principal de onde trabalha, você ama cuidar dos outros e é muito gentil e educada.""",
#     llm= settings.MODEL_PRO,
#     allow_dellegation=True,

# )

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from app.models.register import Prontuario
from app.config.settings import settings




Nini= create_agent(
    model = settings.MODEL_PRO,
    system_prompt=""" Você é uma enfermeira de triagem, colete os dados do paciente e transforme em texto e em JSON para os outros agentes""",
    response_format= Prontuario
)

texto_paciente = """
Paciente João da Silva, 45 anos, masculino, etnia branca.
CPF 12345678901, RG 1234567, nascido em 15/04/1979.
Email joao@email.com, telefone 41999998888, CEP 80000000, região Sul, PR, município Curitiba.
Sem histórico de deslocamento recente.
Relata alergia a dipirona, sem diabetes. Nega doenças genéticas.
Mãe hipertensa. Em uso de omeprazol. Nega cirurgias prévias. Carteira de vacinação em dia.
Peso 82kg, altura 1.75m, tipo O, fator Rh positivo.
Não fumante, consome álcool socialmente, pratica caminhada 3x por semana. Trabalha como contador.
Sinais vitais: PA 120/80 mmHg, FC 75 bpm, SpO2 98%, temperatura 36.5°C, glicemia 95 mg/dL.
"""

pergunta = HumanMessage(content=texto_paciente)
response = Nini.invoke(
    {"messages": [pergunta]}
)

prontuario_validado = response.get("structured_response")

if prontuario_validado:
    print(prontuario_validado.model_dump_json(indent=2))
else:
    print("Resposta recebida do agente:")

    print(response)

    print(response)

