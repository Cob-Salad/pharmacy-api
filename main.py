import json
from fastapi import FastAPI

from models import Patient

with open("patients.json", "r") as f:
    patient_list: list[dict]= json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"

app = FastAPI()

patients: list[Patient] = []

for item in patient_list:
    p = Patient(**item)
    patients.append(p)

@app.get("/patients")
async def get_patients() -> list[Patient]:
    return patients
    #for patient in patient_list:
    #    list_patient.append(Patient.first_name)
    #return list_patient

@app.post("/patients")
async def create_patient(newpatient: Patient) -> None:
    patients.append(newpatient)


@app.put("/patients{first_name}")
async def update_patient(updatedpatient: Patient, first_name: str) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients[i] = updatedpatient
            return
        else:
            patients.append(updatedpatient)
            return

@app.delete("/patients{first_name}")
async def delete_patient(first_name: str):
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients.pop(i)
            return