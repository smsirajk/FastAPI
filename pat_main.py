from fastapi import FastAPI,Path, Query, HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/patients")
def hello():
    return {'message': 'Patients data Management System'}

@app.get("/about")
def about():
    return {'message': 'Fully Functional Patienets management system'}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
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

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of the height, weight, or bmi'), order: str = Query('asc', description='Sort order : asc or desc')):
        valid_fields = ['age', 'admission_date', 'name']
        if sort_by not in valid_fields:
            raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")

        if order not in ['asc', 'desc']:
            raise HTTPException(status_code=400, detail="Invalid order. Valid orders are: asc, desc")

        data = load_data()

        sorted_order = True if order == 'asc' else False

        sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=sorted_order)

        return sorted_data
