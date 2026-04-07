from fastapi import APIRouter , HTTPException , Depends
from jobs.schema import JobResponse,JobCreate
from jobs.model import JobApplication
from sqlalchemy.orm import Session 
from auth.jwt_handler import verify_token
from typing import List
from Database.database import get_db


router = APIRouter(prefix='/jobs',tags = ['Jobs'])


"""
add new job 
"""
@router.post("/",response_model=JobResponse)
def create_job(job:JobCreate,user_id:int,db:Session = Depends(get_db)):
    new_job = JobApplication(
        user_id = user_id,
        company_name= job.company_name,
        role = job.role,
        salary = job.salary,
        status = job.status,
        applied_date = job.applied_date,
        notes = job.notes
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

# show all job 
@router.get('/',response_model=List[JobResponse])
def get_jobs(user_id:int,db:Session = Depends(get_db)):
    jobs = db.query(JobApplication).filter(JobApplication.user_id == user_id).all()
    return jobs

#update the job status
@router.put('/{job_id}')
def update_job_status(job_id : int,job:JobCreate,user_id:int, db:Session = Depends(get_db),):
    existing = db.query(JobApplication).filter(JobApplication.id ==job_id,JobApplication.user_id==user_id).first()
    if not existing:
        raise HTTPException(status_code = 404,detail='JOb not found')
    
    existing.status = job.status
    existing.company_name = job.company_name
    existing.salary= job.salary
    existing.applied_date = job.applied_date
    existing.role = job.role
    # db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing


# delete the job 
@router.delete('/{job_id}')
def delete_job(job_id :int,user_id :int,db:Session = Depends(get_db)):
    existing = db.query(JobApplication).filter(job_id == JobApplication.id,user_id == JobApplication.user_id).first()
    if not existing:
        raise HTTPException(status_code = 404, detail="job not found")
    
    db.delete(existing)
    db.commit()
    return {'message':"job deleted successfully"}