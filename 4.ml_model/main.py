from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
import  pickle
from typing import Literal , Annotated
import pandas as pd
import sklearn.compose._column_transformer as _ct

# Patch for loading models pickled with sklearn 1.6.x in sklearn 1.8+
if not hasattr(_ct, '_RemainderColsList'):
    class _RemainderColsList(list):
        def get_indexer(self, target):
            return list(range(len(target)))
    _ct._RemainderColsList = _RemainderColsList

# import the ml model
with open ('model.pkl','rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# pydantic model to validate the data 

class UserInput(BaseModel):
    age : Annotated[int, Field(...,gt = 0, lt = 100, description= "the age of user")]
    weight :Annotated[float, Field(...,gt = 0, description= "Weight of user")]
    height :Annotated[float, Field(...,gt = 0, lt = 2.5, description= "Height of user")]
    income_lpa: Annotated[float, Field(...,gt = 0, description= "Income  of user")]
    smoker:Annotated[bool, Field(..., description= "user is smoler or not")]
    city:Annotated[str, Field(..., description= "City of user")]
    occupation : Annotated[Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'], Field(..., description= "Occupation of user")]

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


@app.post('/predict')
def predict_premium(data:UserInput):
   input_df = pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        "occupation":data.occupation
    }])
   prediction=model.predict(input_df)
   return JSONResponse(status_code=200,content={'predicted_category':prediction[0]})



        
    