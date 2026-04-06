from pydantic import BaseModel , Field
from typing import Optional

class UserJobApplication(BaseModel):
    company_name :str = Field(...,description="name of company")
    role :str = Field(...,description="Role of job postion")
    salary :int = Field(...,description="Package of company offering")
    status :int = Field(...,Optional=['yes ','no'],description="apllication reject or not")