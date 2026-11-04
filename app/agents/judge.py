import json
from langchain.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434"
)

async def mesclar_analises(prontuario: dict, diagnostico_mimic: str, diagnostico_pub: str) -> str:
    """
    Agente Juiz (Presidente da Junta Médica):
    Recebe os diagnósticos independentes do Especialista MIMIC (Hemodinâmico)
    e do Especialista PubMed (Sintomático/Literatura), arbitra divergências 
    e consolida a decisão clínica definitiva.
    """
    
    system_prompt = """Você é o Presidente da Junta Médica e Diretor Clínico de Elite de um hospital de alta complexidade. 
Seu padrão de exigência é máximo. Você não aceita superficialidade, contradições não resolvidas ou diagnósticos preguiçosos.

Sua função é arbitrar a discussão entre dois especialistas renomados da sua equipe:
- **Especialista A (MIMIC):** Focou a tese diagnóstica nos SINAIS VITAIS, estabilidade fisiológica e padrões de UTI.
- **Especialista B (PubMed):** Focou a tese diagnóstica na SINTOMATOLOGIA, literatura clínica, histórico e diagnósticos diferenciais.

Sua missão é julgar as duas hipóteses, cruzar os dados do prontuário e emitir um PARECER CONSOLIDADO DEFINITIVO.

Estruture seu parecer clínico com clareza clínica e objetividade implacável:

1. **DIAGNÓSTICO CONSOLIDADO DA JUNTA:** O diagnóstico presuntivo principal definitivo que unifica a causa fisiopatológica (Sintomas) com o impacto sistêmico (Sinais Vitais).
2. **ARBITRAGEM E RESOLUÇÃO DE DIVERGÊNCIAS:** Analise os pontos onde os especialistas concordam e onde discordam. Se o Agente A apontou um choque/colapso e o Agente B apontou uma doença específica (ex: Sepse, IAM, Anafilaxia), conecte a causa ao efeito ou descarte a hipótese mais fraca com fundamentação.
3. **NÍVEL DE GRAVIDADE E RISCO SISTÊMICO:** Defina o nível real de urgência clínica do paciente (Baixo, Moderado, Alto, Imediato/Crítico).
4. **DIRETRIZ FINAL PARA A NINI:** Instrução direta e cirúrgica com os pontos-chave para a atribuição final da cor no Protocolo de Manchester.

Seja analítico, assertivo e cirúrgico. Elimine ruídos e entregue a verdade clínica."""

    prontuario_str = json.dumps(prontuario, indent=2, ensure_ascii=False)

    conteudo_analise = f"""
--- PRONTUÁRIO ORIGINAL DO PACIENTE ---
{prontuario_str}

--- TESE DIAGNÓSTICA DO ESPECIALISTA A (HEMODINÂMICA / MIMIC) ---
{diagnostico_a}

--- TESE DIAGNÓSTICA DO ESPECIALISTA B (SINTOMAS E LITERATURA / PUBMED) ---
{diagnostico_b}
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=conteudo_analise)
    ]

    response = await llm.ainvoke(messages)
    return response.content