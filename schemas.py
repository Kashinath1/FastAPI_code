from datetime import date
from typing import Optional, Generic, TypeVar
from uuid import UUID
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


T = TypeVar('T')


# build a schema using pydantic
# Properties required during User creation


class UserSchema(BaseModel):
    id: UUID
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    auth_provider: str
    is_active: bool

    class Config:
        orm_mode = True


# Properties required during Patient creation

class PatientSchema(BaseModel):
    id: UUID
    patient_generalinfo: str
    dental_chart: str
    allergy_history: UUID
    medical_history: str

    class Config:
        orm_mode = True


# Properties required during pain_patient creation

class Patient_allergySchema(BaseModel):
    id: UUID
    allergies_id: UUID
    specific_cause: str
    specific_organs: str
    allergy_time: date

# properties required during pain_history

class allergiesSchema(BaseModel):
    id: UUID
    id1:UUID
    allergy_name: str
    allergy_organ: str
    allergy_cause: str



# Holds properties of Optional field

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


# Holds properties of UserSchema

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


# Holds properties of PatientSchema

class RequestPatient(BaseModel):
    parameter: PatientSchema = Field(...)


# hold this properties of Pain_PatientSchema

class RequestPatient_allergy(BaseModel):
    parameter:  Patient_allergySchema = Field(...)

# holds properties of Pain_historySchema

class Requestallergies(BaseModel):
    parameter: allergiesSchema = Field(...)

  
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
