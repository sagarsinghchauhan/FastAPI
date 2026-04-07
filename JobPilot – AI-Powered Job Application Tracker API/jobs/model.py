from sqlalchemy import Column, Integer, String
from Database.database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    company_name = Column(String, index=True)
    role = Column(String)
    salary = Column(Integer)
    status = Column(String, default="applied")
    applied_date = Column(String)
    notes = Column(String, nullable=True)
