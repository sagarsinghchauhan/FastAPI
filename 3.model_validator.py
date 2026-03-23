from pydantic import BaseModel,model_validator  , EmailStr  
from typing  import Dict , List 

class Patient(BaseModel):
    name:str
    age : int
    email : EmailStr
    weight :float
    married : bool
    allergies : List[str]
    contact_detail :Dict[str, str]

    @model_validator(model = 'after')
    def validate_emergency_contact(cls,model):
        if model.age >60  and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        
        return model


patient_info={'name':'sage','email':'abc@hdfc.com','age':32 ,'weight':58.3,'aligery':['pollen','dust'],
              'contact_details':{'phone_number':'23456'}}


Patient1 = Patient(**patient_info)   # validation -> type coercion


