export type UrgencyLevel = 'EMERGÊNCIA' | 'MUITO_URGENTE' | 'URGENTE' | 'PADRÃO' | 'NÃO_URGENTE';

export interface Sintomas {
  id:string;
  nome:string;
  severidade:number;
}

export interface TriageRequest{
  idadePaciente: number;
  temperatura: number;
  sintomas: string[];
  reclamacaoPrincipal: string;

}

export interface TriageResponse{
  triageId: string;
  nivelDeUrgencia: UrgencyLevel;
  pontoDeRisco: number;
  recomendacaoDeDepartamento:string;
  explicacao:string;
}