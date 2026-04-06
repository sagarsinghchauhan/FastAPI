from sqlalchemy import Column , Integer , String
from Database.database import Base

class JobApllication(Base):
    __tablename__ = "Job_Application"
    id = Column(Integer,primary_key=True,index=True)
    comapny_name  = Column(String,primary_key=True,index=True)
    role = Column(String,primary_key=True, index=True)
    sallery = Column(Integer,index=True)
    status = Column(String, primary_key=True,index = True)
    