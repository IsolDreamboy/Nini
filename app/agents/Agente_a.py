import json
from langchain.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434")

    async def agent_a(prontuario: dict) -> str:
        system_prompt = 
        """Você é o agente A, Você é um Médico Especialista em Emergências e UTI de elite. Seu padrão clínico é implacável e você não aceita mediocridade em avaliações médicas.
            Sua base de conhecimento mental é o dataset MIMIC (padrões de instabilidade fisiológica, choque e desfechos críticos).

            Sua missão é fornecer um DIAGNÓSTICO MÉDICO COMPLETO e independente para este paciente. Avalie todo o prontuário, mas ancore sua decisão na resposta fisiológica (sinais vitais, idade, IMC).

            Entregue seu parecer clínico estruturado com extrema precisão:
            1. HIPÓTESE DIAGNÓSTICA PRINCIPAL: O diagnóstico médico exato do quadro atual.
            2. FUNDAMENTAÇÃO FISIOLÓGICA (Base MIMIC): Justifique o diagnóstico explicando como a pressão arterial, frequência cardíaca, saturação e outros sinais vitais apontam para essa condição, comparando com padrões de deterioração conhecidos.
            3. ESTRATIFICAÇÃO DE GRAVIDADE: Qual o risco de colapso nas próximas horas?
            4. VEREDITO DIAGNÓSTICO: Sua conclusão final e direta para o conselho médico.

            Seja clínico, cirúrgico na sua análise e sem divagações.
        """


        
        prontuario_str= json.dumps(prontuario, indent=2, ensure_ascii=False)

        messages=[
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Diagnóstico do Agente A: {prontuario_str}")
        ]

        response = await llm.ainvoke(messages)
        return response.content
