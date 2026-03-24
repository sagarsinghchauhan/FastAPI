from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
import  json 
from typing import Annotated , Literal

app = FastAPI()

class Paitent(BaseModel):
    id :Annotated[str, Field(..., description= 'Id of the patient',examples=['p001'])]
    name : Annotated[str , Field(...,description='Name of the user')]
    city : Annotated[str , Field(...,description='city name where the patient is living  ')]
    age : Annotated[int , Field(...,gt = 0, lt = 120, description='Age of the user')]
    gender: Annotated[Literal['Male','Female','other'], Field(...,description='Gender of the patient')]
    weight : Annotated[float ,  Field(...,gt = 0, description='weight of the patient in mtrs')]
    height : Annotated[float , Field(...,gt = 0,description='height of the patient in kgs')]
    
    @computed_field
    @property
    def bmi (self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi 
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi <18.5:
            return "underweight"
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi <30 :
            return "Normal"
        else :
            return "obses"

def load_data():
    with open(r'D:\FastAPI\patients.json','r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open(r'D:\FastAPI\patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hellow():
    return {'message':'Pateint Management sysetm api'}

@app.get('/about')
def about():
    pass


@app.get("/sort")
def sort_patients(sort_by : str = Query(...,description = 'Sort on the basis of height , weight or bmi'),order:str = Query('asc',description="Sort in asc and desc order")):
    valid_feilds = ['height','weight','bmi']
    if sort_by not in valid_feilds:
        raise HTTPException(status_code= 400,detail = f'Invaild field select from {valid_feilds}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail = f'invalid order selet between asc and desc')
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient:Paitent):

    # load existing data 
    data = load_data()

    # check if the patient already exists 
    if patient.id in data:
        raise HTTPException(status_code=400, detail = 'Patient already exists')
    
    # new patient add to the database
    data[patient.id]=patient.model_dump(exclude=['id'])

    # save into the json file 
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'pateint created sucessfully '})









