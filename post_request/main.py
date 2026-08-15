from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import  Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the Patients')]
    gender: Annotated[Literal['Male','Female','others'], Field(...,description='Gender of the Patients')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patients in mtrs')]
    weight: Annotated[float, Field(..., description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height **2),2)
        return bmi

    @computed_field
    @property
    def vertict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Close'

def laod_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data, f)




@app.get("/")
def welcome():
    return {'message':'Patient Management system API'}

@app.get('/about')
def about():
    return {'message':'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = laod_data()
    return data

@app.post('/create')
def create_patient(patient: Patient):
    #load existing data
    data = laod_data()

    # Check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient alrady exists')

    # New patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)
    return JSONResponse(status_code=201, content={'message':'Patient created successfully !!!'})

