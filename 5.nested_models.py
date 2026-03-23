from pydantic import BaseModel

class Address(BaseModel):
    city :str
    state :str
    pin : int


class Patient(BaseModel):
    name:str
    gender : str
    age: int
    address : Address


addresss_dict = {'city':'gudgao','state':'haryana','pin':12356}

address1 = Address(**addresss_dict)

patient_dic = {'name':'sagar','gender':'male','age':23,'address':address1}

patient1 = Patient(**patient_dic)

print(patient1.address, patient1.name)
print(patient1)