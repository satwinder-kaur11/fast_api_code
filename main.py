from pydantic import BaseModel
from typing import List
from typing import Dict,Optional
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies:Optional[List[str]] = None 
    contact_details: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)

patient_info = {
                "name":"satwinder",
                "age":12,
                "weight":49.9,
                "married":"no",
                "allergies" : ['pollen','dust'],
                'contact_details':{'email':'abc@gmail.com',
                                   'phone':'3456793266'}
                }

patient1 = Patient(**patient_info)
insert_patient_data(patient1)
