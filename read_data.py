import json

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data 

print(load_data())