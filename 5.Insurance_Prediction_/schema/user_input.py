from typing import Literal , Annotated
from pydantic import BaseModel , Field , computed_field , field_validator
from config.city_tier import tier_1_cities, tier_2_cities





# pydantic model to validate the data 

class UserInput(BaseModel):
    age : Annotated[int, Field(...,gt = 0, lt = 100, description= "the age of user")]
    weight :Annotated[float, Field(...,gt = 0, description= "Weight of user")]
    height :Annotated[float, Field(...,gt = 0, lt = 2.5, description= "Height of user")]
    income_lpa: Annotated[float, Field(...,gt = 0, description= "Income  of user")]
    smoker:Annotated[bool, Field(..., description= "user is smoler or not")]
    city:Annotated[str, Field(..., description= "City of user")]
    occupation : Annotated[Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'], Field(..., description= "Occupation of user")]


    @field_validator('city')
    @classmethod
    def normalize_city(cls,v:str)->str:
        v = v.strip().title()
        return v
    
    @computed_field
    @property
    def bmi (self)->float:
        bmi = round(self.weight/(self.height)**2,2)
        return bmi 
    


    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30 :
            return "high"
        elif self.smoker or self.bmi > 27:
            return 'medium'
        else :
            return 'low'
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age <25 :
            return 'young'
        elif self.age < 45: 
            return 'adult'
        elif self.age < 60 :
            return 'middle_aged'
        return 'senior'
    
    @computed_field
    @property 
    def city_tier(self) ->int:
        if self.city in tier_1_cities :
            return 1
        elif self.city  in tier_2_cities:
            return 2
        else:
            return 3
