# put 
from fastapi import FastAPI , Path , HTTPException , Query 
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field 
import  json 
from typing import Annotated , Literal , Optional

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
        
class Update_patient(BaseModel):
    name : Annotated[Optional[str] , Field(default=None,description='Name of the user')]
    city : Annotated[Optional[str] , Field(default=None,description='city name where the patient is living  ')]
    age : Annotated[Optional[int] , Field(default=None,gt = 0, lt = 120, description='Age of the user')]
    gender: Annotated[Optional[Literal['Male','Female']], Field(default=None,description='Gender of the patient')]
    weight : Annotated[Optional[float] ,  Field(default=None,gt = 0, description='weight of the patient in mtrs')]
    height : Annotated[Optional[float] , Field(default=None,gt = 0,description='height of the patient in kgs')]
    

   


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
    data[patient.id]=patient.model_dump(exclude={'id'})

    # save into the json file 
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'pateint created sucessfully '})

@app.put('/edit/{patient_id}')
def update_patient(patient_id:str, patient_update:Update_patient):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = "Patient not found")
    
    existing_patient_info = data[patient_id]

    updateed_patenent_info = patient_update.model_dump(exclude_unset=True)

    for key , value in updateed_patenent_info.items():
        existing_patient_info[key] = value
    
    # existing_patient_info-> pydantic objext -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Paitent(**existing_patient_info)

    # -> pydantic object -> dict 
    existing_patient_info=patient_pydantic_object.model_dump(exclude={'id'})
    # add this dict to data
    data[patient_id] = existing_patient_info

    #save data
    save_data(data)
    
    return JSONResponse(status_code = 200, content = {'message':"patient update " })


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id :str):
    #load_data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code= 404,detail="Patient not found"  )
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=200, content={'message': "patient deleted"})
