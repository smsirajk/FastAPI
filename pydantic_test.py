from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted .... the data')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated the data')

patient_info = {'name': 'John Doe', 'age': 30}

patient1 = Patient(**patient_info)

insert_patient(patient1)

update_patient(patient1)