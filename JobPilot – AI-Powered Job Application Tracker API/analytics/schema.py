from pydantic import BaseModel , Field
# from typing

class Summary(BaseModel):
    total_applied: int
    interview :int
    offer :int
    rejected: int 
    pending : int

class Resume_detail(BaseModel):
    resume :str
    job_description :str

class Resume_score(BaseModel):
    match_score :float
    verdict : str


