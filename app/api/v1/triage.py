from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.connection import get_db
from app.db.models import ProntuarioDB
from app.models.register import Prontuario
from app.services.triage_engine import run_nini_triage, TriageResult
import uuid

router = APIRouter(prefix="/triagem", tags=["Triagem"])

@router.get("/prontuarios", status_code=status.HTTP_200_OK)
def listar_prontuarios(db: Session = Depends(get_db)):
    """Retorna todos os prontuários e triagens registrados no banco."""
    prontuarios = db.query(ProntuarioDB).order_by(ProntuarioDB.criado_em.desc()).all()
    return prontuarios

@router.post("/processar", status_code=status.HTTP_201_CREATED)
async def processar_triagem(
    prontuario: Prontuario, 
    db: Session = Depends(get_db)
):
    try:
        id_temp = str(uuid.uuid4())
        
        nini_result: TriageResult = await run_nini_triage(
            paciente_id=id_temp,
            prontuario=prontuario.model_dump()
        )

        
        novo_prontuario = ProntuarioDB(
            # Retornos da IA
            diagnostico_ia=getattr(nini_result, "diagnostico", str(nini_result)),
            classificacao_risco=getattr(nini_result, "classificacao_risco", "Indefinido"),

            # 1. Registro Paciente
            nome_completo=prontuario.registro.nome_completo,
            nome_social=prontuario.registro.nome_social,
            cpf=prontuario.registro.cpf,
            rg=prontuario.registro.rg,
            data_de_nascimento=prontuario.registro.data_de_nascimento,
            sexo_biologico=prontuario.registro.sexo_biologico,
            etnia=prontuario.registro.etnia,
            email=prontuario.registro.email,
            telefone=prontuario.registro.telefone,
            cep=prontuario.registro.cep,
            complemento_cep=prontuario.registro.complemento_cep,
            regiao=prontuario.registro.regiao,
            uf=prontuario.registro.uf,
            municipio=prontuario.registro.municipio,
            historico_de_deslocamento=prontuario.registro.historico_de_deslocamento,

            # 2. Triagem e Sintomas
            sintomas=prontuario.sintomas.sintomas,
            alergias=prontuario.triagem.alergias,
            diabetes=prontuario.triagem.diabetes,
            doencas_geneticas=prontuario.triagem.doencas_geneticas,
            historico_familiar=prontuario.triagem.historico_familiar,
            historico_clinico_geral=prontuario.triagem.historico_clinico_geral,
            medicamento_em_uso=prontuario.triagem.medicamento_em_uso,
            cirurgia_previas=prontuario.triagem.cirurgia_previas,
            status_vacinal=prontuario.triagem.status_vacinal,
            grupo_de_risco=prontuario.triagem.grupo_de_risco,
            historico_de_viagens_recente=prontuario.triagem.historico_de_viagens_recente,

            # 3. Antropometria
            peso=prontuario.antropometria.peso,
            altura=prontuario.antropometria.altura,
            imc=prontuario.antropometria.imc,
            tipo_sanguineo=prontuario.antropometria.tipo_sanguineo,
            fator_rh=prontuario.antropometria.fator_rh,

            # 4. Estilo de Vida
            fumante=prontuario.estilo_de_vida.fumante,
            alcoolico=prontuario.estilo_de_vida.alcoolico,
            atividades_fisicas=prontuario.estilo_de_vida.atividades_fisicas,
            habitos_alimentares=prontuario.estilo_de_vida.habitos_alimentares,
            dados_demograficos=prontuario.estilo_de_vida.dados_demograficos,
            ocupacao_profissional=prontuario.estilo_de_vida.ocupacao_profissional,

            # 5. Sinais Vitais
            frequencia_cardiaca=prontuario.sinais_vitais.frequencia_cardiaca,
            pressao_arterial=prontuario.sinais_vitais.pressao_arterial,
            saturacao_de_oxigenio=prontuario.sinais_vitais.saturacao_de_oxigenio,
            temperatura_corporal=prontuario.sinais_vitais.temperatura_corporal,
            glicemia=prontuario.sinais_vitais.glicemia,
        )

        # 3. Grava no banco e gera o UUID primário
        db.add(novo_prontuario)
        db.commit()
        db.refresh(novo_prontuario)

        
        return {
            "status": "completed",
            "paciente_id": novo_prontuario.id,
            "triage_result": nini_result
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no processamento da triagem: {str(e)}"
        )