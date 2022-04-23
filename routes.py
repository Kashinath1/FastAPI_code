from datetime import date
import shutil
from uuid import UUID
from fastapi import APIRouter, File, UploadFile
from fastapi import Depends
from fastapi_sqlalchemy import db
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import (
                      RequestPatient, Requestallergies,
                      RequestUser, RequestPatient_allergy, Response)

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# USER TABLE Routes
# Defining path operation for /user/create
@router.post("/user/create")
async def create_user_service(id: UUID, email: str, first_name: str,
                              last_name: str, is_verified: bool,
                              auth_provider: str, is_active: bool,
                              db: Session=Depends(get_db),
                              file: UploadFile=File(...)):
    with open("media/" + file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
    url = str("media/" + file.filename)

    return crud.create_user(db=db, id=id, email=email, first_name=first_name,
                            last_name=last_name, is_verified=is_verified,
                            auth_provider=auth_provider, is_active=is_active,
                            profile_pic=url)


# Defining path operation for /user
@router.get("/user")
async def get_users(db: Session=Depends(get_db)):
    _users = crud.get_user(db)
    return Response(status="Ok", code="200", message="Success fetch all data",
                    result=_users)


# Defining path operation for /user/{userID}
@router.get("/user/{userID}")
async def get_by_user_id(id: UUID, db: Session=Depends(get_db)):
    _users = crud.get_user_by_id(db, id)
    return Response(status="OK", code=200, message="Success fetch with id",
                    result=_users)


# Defining path operation for /user/update
@router.patch("/user/update/")
async def update_user(id: UUID, email: str, first_name: str, last_name: str,
                      is_verified: bool, auth_provider: str, is_active: bool,
                      db: Session=Depends(get_db),
                      file: UploadFile=File(...)):
    with open("media/updated/"+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
    url = str("media/updated/"+file.filename)

    return crud.update_user(db=db, email=email, first_name=first_name,
                            last_name=last_name, is_verified=is_verified,
                            auth_provider=auth_provider, is_active=is_active,
                            profile_pic=url, user_id=id)


# Defining path operation for /user/delete
@router.delete("user/delete")
async def delete_user(request: RequestUser,  db: Session=Depends(get_db)):
    crud.remove_user(db, user_id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)


# PATIENT TABLE
# Defining path operation for /patient/create
@router.post("/patient/create")
async def create_patient_service(id: UUID, patient_generalinfo: str,
                                 dental_chart: str, allergy_history: UUID,
                                 medical_history: str,
                                 db: Session=Depends(get_db)):
    return crud.create_patient(db=db, id=id,
                               patient_generalinfo=patient_generalinfo,
                               dental_chart=dental_chart,
                               allergy_history=allergy_history,
                               medical_history=medical_history)


# Defining path operation for /patient
@router.get("/patient")
async def get_patient(db: Session=Depends(get_db)):
    _patients = crud.get_patient(db)
    return Response(status="OK", code="200",
                    message="Success fetch all data of patient",
                    result=_patients)


# Defining path operation for /patient/{patientID}
@router.get("/patient/{patientID}")
async def get_by_patient_id(id: UUID, db: Session=Depends(get_db)):
    _patient = crud.get_patient_by_id(db, id)
    return Response(status="OK", code=200,
                    message="Success fetch data with id", result=_patient)


# Defining path operation for /patient/update
@router.patch("/patient/update")
async def update_patient(id: UUID, patient_generalinfo: str, dental_chart: str,
                         allergy_history: UUID, medical_history: date,
                         db: Session=Depends(get_db)):
    return crud.update_patient(db=db, id=id,
                               patient_generalinfo=patient_generalinfo,
                               dental_chart=dental_chart,
                               allergy_history=allergy_history,
                               medical_history=medical_history)


# Defining path operation for /patient/delete
@router.delete("/patient/delete")
async def delete_patient(request: RequestPatient,
                         db: Session=Depends(get_db)):
    crud.remove_patient(db, patient_id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)


# routing path for pain_patient
@router .get("/patient_allergy")
async def get_patient_allergy(db: Session=Depends(get_db)):
    _patient_allergy = crud.get_patient_allergy(db)
    return Response(status="OK", code="200",
                    message="Success fetch all data of patient",
                    result=_patient_allergy)

# Defining path operation for /pain_patient/{pain_patient ID}


@router.get("/patient_allergy/{patientID}")
async def get_patient_allergy_by_id(id: UUID, db: Session=Depends(get_db)):
    _patient_allergy = crud.get_patient_allergy_by_id(db, id)
    return Response(status="OK", code=200,
                    message="Success fetch data with id",
                    result=_patient_allergy)


# post method for patient_allergy method
@router.post("/patient_allergy/create")
async def create_patient_allergy(id: UUID, allergies_id: UUID,
                                 specific_cause: str,
                                 specific_organs: str, allergy_time: date,
                                 db: Session=Depends(get_db)):
    return crud.create_patient_allergy(db=db, id=id, allergies_id=allergies_id,
                                       specific_cause=specific_cause,
                                       specific_organs=specific_organs,
                                       allergy_time=allergy_time)


# Defining path operation for /pain_patient/update
@router.patch("/patient_allergy/update")
async def update_patient_allergy(id: UUID, allergies_id: UUID,
                                 specific_cause: str,
                                 specific_organs: str, allergy_time: date,
                                 db: Session=Depends(get_db)):
    return crud.update_patient_allergy(db=db, id=id, allergies_id=allergies_id,
                                       specific_cause=specific_cause,
                                       specific_organs=specific_organs,
                                       allergy_time=allergy_time)


# Defining path operation for /pain_patient/delete
@router.delete("/patient_allergy/delete")
async def delete_patient_allergy(request: RequestPatient_allergy,
                                 db: Session=Depends(get_db)):
    crud.remove_patient_allergy(db, id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)

# # post method for alergies


@router.post("/alergies/create")
async def create_allergies(id: UUID, id1: UUID,
                           allergy_name: str,
                           allergy_organ: str,
                           allergy_cause: str,
                           db: Session=Depends(get_db)):
    return crud.create_allergies(db=db, id=id, id1=id1,
                                 allergy_name=allergy_name,
                                 allergy_organ=allergy_organ,
                                 allergy_cause=allergy_cause)

# get  routs for alergies


@router .get("/alergies")
async def get_allergies(db: Session=Depends(get_db)):
    _pain_history = crud.get_allergies(db)
    return Response(status="OK", code="200",
                    message="Success fetch all data of patient",
                    result=_pain_history)


# Defining path operation for /pain_history/{pain_patient ID}
@router.get("/alergies/{get_allergies_by_id}")
async def get_allergies_by_id(id: UUID, db: Session=Depends(get_db)):
    _alergies = crud.get_allergies_by_id(db, id)
    return Response(status="OK", code=200,
                    message="Success fetch data with id", result=_alergies)

# post method for alergies


@router.post("/alergies/create")
async def create_allergies(id: UUID, id1: UUID,
                              allergy_name: str,
                              allergy_organ: str,
                              allergy_cause: str,
                              db: Session=Depends(get_db)):
    return crud.create_allergies(db=db, id=id, id1=id1,
                                    allergy_name=allergy_name,
                                    allergy_organ=allergy_organ,
                                    allergy_cause=allergy_cause)

# delete method for alergies


@router.delete("/alergies/delete")
async def delete_alergies(request: Requestallergies,
                              db: Session=Depends(get_db)):
    crud.remove_allergies(db, id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)

# patch method for alergies


@router.patch("/alergies/update")
async def update_allergies(id: UUID, id1: UUID,
                              allergy_name: str,
                              allergy_organ: str,
                              allergy_cause: str,
                              db: Session=Depends(get_db)):
    return crud.update_allergies(db=db, id=id, id1=id1,
                                    allergy_name=allergy_name,
                                    allergy_organ=allergy_organ,
                                    allergy_cause=allergy_cause)
