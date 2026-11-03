from sqlalchemy import Column, String, Integer, Float, Boolean, JSON, DateTime
from datetime import datetime
import uuid
from app.db.connection import Base 

class ProntuarioDB(Base):
    __tablename__ = "prontuarios_triagem"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    criado_em = Column(DateTime, default=datetime.utcnow)

    # Retornos da IA (Nini)
    diagnostico_ia = Column(String, nullable=True)
    classificacao_risco = Column(String, nullable=True)

    # Dados do Paciente (Registro)
    nome_completo = Column(String, nullable=False)
    nome_social = Column(String, nullable=True)
    cpf = Column(String, unique=True, index=True, nullable=False)
    rg = Column(String, nullable=False)
    data_de_nascimento = Column(String, nullable=False)
    sexo_biologico = Column(String, nullable=False)
    etnia = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    complemento_cep = Column(String, nullable=True)
    regiao = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    municipio = Column(String, nullable=False)
    historico_de_deslocamento = Column(String, nullable=False)

    # Triagem e Sintomas
    sintomas = Column(JSON, default=list)
    alergias = Column(JSON, default=list)
    diabetes = Column(Boolean, default=False)
    doencas_geneticas = Column(String, nullable=True)
    historico_familiar = Column(String, nullable=False)
    historico_clinico_geral = Column(String, nullable=False)
    medicamento_em_uso = Column(JSON, default=list)
    cirurgia_previas = Column(JSON, default=list)
    status_vacinal = Column(String, nullable=False)
    grupo_de_risco = Column(Boolean, default=False)
    historico_de_viagens_recente = Column(String, nullable=True)

    # Antropometria
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    imc = Column(Float, nullable=False)
    tipo_sanguineo = Column(String, nullable=False)
    fator_rh = Column(String, nullable=False)

    # Estilo de Vida
    fumante = Column(Boolean, default=False)
    alcoolico = Column(Boolean, default=False)
    atividades_fisicas = Column(String, nullable=False)
    habitos_alimentares = Column(String, nullable=False)
    dados_demograficos = Column(String, nullable=False)
    ocupacao_profissional = Column(String, nullable=False)

    # Sinais Vitais
    frequencia_cardiaca = Column(Integer, nullable=False)
    pressao_arterial = Column(String, nullable=False)
    saturacao_de_oxigenio = Column(Integer, nullable=False)
    temperatura_corporal = Column(Float, nullable=False)
    glicemia = Column(Integer, nullable=False)