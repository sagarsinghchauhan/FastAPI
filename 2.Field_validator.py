from pydantic import BaseModel , Field  , AnyUrl , EmailStr , field_validator
from typing import Dict, List , Optional, Annotated


class Patient(BaseModel):
    name : str
    age : int 
    email : EmailStr
    weight : float
    aligery : List[str]
    contact_details : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_email = ['hdfc.com','icici.com']
        # abc@gmail.com
        domani_speicfic = value.split('@')[-1]
        print(domani_speicfic)

        if domani_speicfic not in valid_email:
            raise ValueError("Not a vaild doamin ")
        
        return value
    
    @field_validator("name")
    @classmethod
    def name_validator(cls,value):
        return value.upper()
    
    @field_validator('age',mode = 'after')
    @classmethod
    def validate_age(cls,value):
        if 0< value and  value <100:
            return value
        else :
            raise ValueError('age should be in between 0 and 100')
    



patient_info={'name':'sage','email':'abc@hdfc.com','age':32 ,'weight':58.3,'aligery':['pollen','dust'],
              'contact_details':{'phone_number':'23456'}}


Patient1 = Patient(**patient_info)   # validation -> type coercion
