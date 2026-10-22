from pydantic import BaseModel,Field, EmailStr, model_validator
from typing import List, Optional

class Sintomas(BaseModel):
  sintomas:str
  

class RegistroPaciente(BaseModel):
  nome_completo: str
  nome_social: Optional[str] = None
  cpf:str = Field(..., pattern=r"^\d{11}$")
  rg:str
  data_de_nascimento:str
  sexo_biologico:str
  etnia:str
  email: EmailStr
  telefone: str
  cep: str
  complemento_cep: Optional[str] = None
  regiao: str
  uf:str = Field(...,max_length=2)
  municipio:str = Field(...)
  historico_de_deslocamento:str


class TriagemPaciente(BaseModel):
  alergias: List[str] = []
  diabetes: bool = False
  doencas_geneticas: Optional[str] = None
  historico_familiar:str 
  historico_clinico_geral: str
  medicamento_em_uso: List[str] = []
  cirurgia_previas: List[str] = []
  status_vacinal: str
  grupo_de_risco: bool = False
  historico_de_viagens_recente: Optional[str] = None


class DadosAntropometria(BaseModel):
  peso: float = Field(..., gt=0, description = "Peso em KG")
  altura: float =  Field(..., gt=0, description = "Altura em Metros")
  imc: float = Field(default= 0.0, description = "Índice de Massa Corporal")
  tipo_sanguineo: str
  fator_rh: str

  @model_validator(mode='after')
  def calcular_imc(self):
    if self.peso> 0 and self.altura > 0:
      self.imc= round(self.peso / (self.altura**2), 2)
    return self

class DadosEstiloDeVida(BaseModel):
  fumante: bool = False
  alcoolico: bool = False
  atividades_fisicas: str
  habitos_alimentares: str
  dados_demograficos: str
  ocupacao_profissional: str


class SinaisVitais(BaseModel):
  frequencia_cardiaca: int = Field(...,description="BPM")
  pressao_arterial: str = Field(..., pattern = r"^\d{2,3}/\d{2,3}$")
  saturacao_de_oxigenio: int = Field(..., ge=0, le=100)
  temperatura_corporal: float = Field(..., ge=30, le=45)
  glicemia: int = Field(..., description = "Dextro")


class Prontuario(BaseModel):
  registro : RegistroPaciente
  triagem : TriagemPaciente
  antropometria : DadosAntropometria
  sinais_vitais : SinaisVitais
  estilo_de_vida : DadosEstiloDeVida