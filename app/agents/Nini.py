import json
import asyncio
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config.settings import settings


#outros agentes

from app.agents.MimicAgent import mimic_agent
from app.agents.PubAgent import pub_agent
from app.agents.Judge import Juiz

class TriageResult(BaseModel):
    manchester_cor: str = Field(description="Cor do Protocolo de Manchester(Vermelho, Laranja, Amarelo, Verde ou Azul)")
    pontuacao_de_risco: float = Field(description="Pontuação de risco de 0.0 a 1.0")
    resumo_clinico: str = Field(description= "Resumo clínico final consubstanciado")
    acao_recomendada: str = Field(description="Conduta médica recomendada (ex: Encaminhamento para Sala Vermelha)")

llm = ChatGoogleGenerativeAI(model=settings.MODEL_PRO)
nini_final_agent = llm.with_structured_output(TriageResult)

async def run_nini_triage(prontuario: dict, paciente_id: str = None) -> TriageResult:
    """
    Orquestrador da pipe Multi-Agente da Nini:
    1. Recebe o prontuário validado da API.
    2. Executa os agentes MIMIC e PubMed em paralelo.
    3. Envia os pareceres ao Agente Juiz para mesclagem e validação.
    4. Nini gera a decisão clínica final formatada.
    """

    diagnostico_mimic,diagnostico_pub = await asyncio.gather(
        mimic_agent.run(prontuario),
        pub_agent.run(prontuario)
    )

    diagnostico_juiz = await mesclar_analises(
        prontuario=prontuario,
        diagnostico_mimic=diagnostico_mimic,
        diagnostico_pub=diagnostico_pub
    )


    system_prompt= f"""Você é a Nini, IA Chefe de Triagem Médica e Responsável pelo Atendimento Clínico.
Sua missão é emitir a classificação final de risco baseada no Protocolo de Manchester.

DIRETRIZES DE COMUNICAÇÃO E PERSONALIDADE:
1. **Rigor Técnico:** Mantenha precisão científica impecável na fundamentação dos sinais vitais e achados clínicos.
2. **Empatia e Gentileza:** Redija o resumo clínico e a ação recomendada utilizando linguagem humanizada, acolhedora e respeitosa, priorizando a segurança e o conforto do paciente.
3. **Clareza Institucional:** O parecer deve ser perfeitamente compreensível para a equipe de enfermagem/médica e transmitir serenidade quanto aos procedimentos indicados.

--- PARECER CONSOLIDADO DO AGENTE JUIZ ---
{diagnostico_juiz}"""

    prontuario_str = json.dumps(prontuario, indent=2, ensure_ascii=False)
    mensagem_usuario = HumanMessage(content=f"Prontuário do Paciente: {prontuario_str}")

    resultado_final = await nini_final_agent.ainvoke([system_prompt, mensagem_usuario])
    return resultado_final