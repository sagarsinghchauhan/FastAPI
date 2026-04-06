from fastapi import APIRouter , HTTPException , Depends
from jobs.schema import UserJobApplication
from jobs.model import JobApllication 

router = APIRouter(prefix='/jobs',tags = ['Job'])

@router.post("/updateJobapplicaton",response_model=UserJobApplication)
def update_job_apllication(user:)