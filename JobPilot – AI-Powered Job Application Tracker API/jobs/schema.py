from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal

class JobCreate(BaseModel):
    company_name: str = Field(..., min_length=1, description="Name of company")
    role: str = Field(..., min_length=1, description="Role of job position")
    salary: int = Field(..., gt=0, description="Package offered by company")
    status: Literal["applied", "interview", "offer", "rejected"] = "applied"
    applied_date: str = Field(..., description="Date when applied (YYYY-MM-DD)")
    notes: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    user_id: int
    company_name: str
    role: str
    salary: int
    status: str
    applied_date: str
    notes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
