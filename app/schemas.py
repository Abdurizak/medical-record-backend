from pydantic import BaseModel
from typing import List, Optional

class AppointmentBase(BaseModel):
    date: str
    reason: str
    doctor_id: int
    patient_id: int

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    medical_history: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    appointments: List[Appointment] = []

    class Config:
        orm_mode = True

class DoctorBase(BaseModel):
    name: str
    specialty: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    appointments: List[Appointment] = []

    class Config:
        orm_mode = True