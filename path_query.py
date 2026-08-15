from fastapi import FastAPI, Path, HTTPException
import json 

app = FastAPI()

#loading the data from the json file

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/about")
def about():
    return {'message': 'This is a Patient Management System built with FastAPI.'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description ='ID of the patient in the DB',
                                        examples = 'P001')):
    data = load_data()

    # Case 1: data is a dict keyed by patient_id
    if isinstance(data, dict):
        if patient_id in data:
            return data[patient_id]
        return {"error": "Patient not found"}

    # Case 2: data is a list of dicts
    if isinstance(data, list):
        for patient in data:
            if str(patient.get("patient_id")) == patient_id:
                return patient
        return {"error": "Patient not found"}

    raise HTTPException(status_code=404, detail='error!:Patient not found')
    