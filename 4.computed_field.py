
from pydantic import BaseModel,model_validator  , EmailStr  , computed_field
from typing  import Dict , List 

class Patient(BaseModel):
    name:str
    age : int
    email : EmailStr
    weight :float
    height : float
    married : bool
    allergies : List[str]
    contact_detail :Dict[str, str]
    

    @model_validator(mode= 'after')
    def validate_emergency_contact(cls,model):
        if model.age >60  and 'emergency' not in model.contact_detail:
            raise ValueError('Patients older than 60 must have an emergency contact')
        
        return model

    @computed_field
    @property
    def bmi(self) ->float:
        bmi = round(self.weight /(self.height ** 2),2)
        return bmi
    


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('bmi' , patient.bmi)
    print('updated')

patient_info={'name':'sage','email':'abc@hdfc.com','age':32 ,'weight':58.3,'allergies':['pollen','dust'],
              'married':True,'height':1.52,
              'contact_detail':{'phone_number':'23456'}}


Patient1 = Patient(**patient_info)   # validation -> type coercion

update_patient_data(Patient1)



