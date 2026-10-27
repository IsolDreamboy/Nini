from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.register import Prontuario as ptr
from app.services.triage_engine import run_nini_triage, TriageResult

router = APIRouter(prefix="/api/v1/triage", tags = ["Triagem"])

class TriagePayload(BaseModel):
  paciente_id: int
  sintomas: str
  ptr:str

class TriageResponse(BaseModel):
  status: str
  paciente_id: int
  triage_result:TriageResult

@router.post("/", response_model=TriageResponse)
async def create_triage(payload: TriagePayload):
  try:

    nini_result= await run_nini_triage(
      paciente_id= payload.paciente_id,
      sintomas= payload.sintomas,
      prontuario= payload.ptr
    )

    return TriageResponse(
      status="completed",
      paciente_id=payload.paciente_id,
      triage_result=nini_result
    )
    
  except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no processamento da triagem: {str(e)}")