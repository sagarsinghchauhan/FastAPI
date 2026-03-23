"""
this is full crash course about pydantic libray
"""
from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List  , Dict, Optional , Annotated

class Patient(BaseModel):  # step 1
    name : Annotated[str,Field(max_length=50, title="name of patient", description="give the name of the patient in less tha 50 words",
                               examples=['sagar','amit'])]
    
    email:EmailStr
    linkdin_url : AnyUrl
    age : int = Field(gt = 0, lt = 120)
    weight : Annotated[float,Field(gt = 0,strict=True)]
    married : Annotated[bool, Field(default=False, description="Is the patient married or not ")]
    allergies : Annotated[Optional[List[str]] , Field(default=None,max_length= 5)]
    contact_detail : Dict[str,str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("inserted into database")

# insert_patient_data('sagar',"30")

patient_into={'name':'sage','age':32 ,'weight':58.3,'married':0,'allergies':['pollen','dust'],
              'contact_detail':{'phone_number':'23456'}
              ,'email':'dfg@gmail.com'}


patient1 = Patient(**patient_into)  # step 2

insert_patient_data(patient1)
