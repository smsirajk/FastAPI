from fastapi import FastAPI,Path
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")

def hello():
    return {'message': 'Hello World'}


@app.get("/about")

def about():
    return {'message': 'This is a FastAPI application.'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description ='ID of the patient in the DB',
                                        example = 'P001')):
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

    return {"error": "Invalid data format"}

