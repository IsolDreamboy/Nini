from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from app.config.settings import settings

class TriageResult(BaseModel):
    manchester_cor: str = Field(
        description="Cor do Protocolo de Manchester: Vermelho, Laranja, Amarelo, Verde ou Azul"
    )
    pontuacao_de_risco: float = Field(
        description="Pontuação de risco calculada de 0.0 a 1.0"
    )
    resumo_clinico: str = Field(
        description="Resumo clínico objetivo justificando a classificação"
    )
    acao_recomendada: str = Field(
        description="Ação imediata recomendada (ex: Encaminhamento para Sala Vermelha)"
    )

async def run_nini_triage(paciente_id: int, sintomas: str, prontuario: str) -> TriageResult:
   
    llm = settings.MODEL_PRO
    structured_llm = llm.with_structured_output(TriageResult)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Você é o motor de triagem do sistema Nini. Analise o prontuário e os sintomas informados "
            "e classifique o nível de urgência do paciente utilizando o Protocolo de Manchester."
        ),
        (
            "human",
            "ID do Paciente: {paciente_id}\n"
            "Sintomas Atuais: {sintomas}\n"
            "Prontuário/Histórico: {prontuario}"
        )
    ])

    triage_chain = prompt | structured_llm

    response = await triage_chain.ainvoke({
        "paciente_id": paciente_id,
        "sintomas": sintomas,
        "prontuario": prontuario
    })
    return response