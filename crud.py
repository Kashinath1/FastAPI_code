# from audioop import add
from datetime import date
from uuid import UUID
from sqlalchemy.orm import Session
from models import (PatientTable, UserTable,
                    Patient_allergy, Allergies_class)
import models


# USER TABLE
# Creating function to get information of all users
def get_user(db: Session):
    return db.query(UserTable).all()


# Creating fuction to get information of user by userID
def get_user_by_id(db: Session, user_id: UUID):
    return db.query(UserTable).filter(UserTable.id == user_id).first()


# Creating function to create user and add it to the database and commit it
def create_user(db: Session, id: UUID, email: str, first_name: str,
                last_name: str, is_verified: bool, auth_provider: str,
                is_active: bool, profile_pic: str):
    db_user = models.UserTable(id=id, email=email, first_name=first_name,
                               last_name=last_name, is_verified=is_verified,
                               auth_provider=auth_provider,
                               is_active=is_active,
                               profile_pic=profile_pic)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Creating function to remove  user by userID
def remove_user(db: Session, user_id: UUID):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


# Creating function to update user informations
def update_user(db: Session, user_id: UUID, email: str, first_name: str,
                last_name: str, is_verified: bool, auth_provider: bool,
                is_active: bool, profile_pic: str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.email = email
    _user.first_name = first_name
    _user.last_name = last_name
    _user.is_verified = is_verified
    _user.profile_pic = profile_pic
    _user.auth_provider = auth_provider
    _user.is_active = is_active

    db.commit()
    db.refresh(_user)
    return _user


# PATIENT TABLE
# Creating function to get information of all patient
def get_patient(db: Session):
    return db.query(PatientTable).all()


# Creating funciton to get information of patient by patientID
def get_patient_by_id(db: Session, patient_id: UUID):
    return db.query(PatientTable).filter(PatientTable.id == patient_id).first()


# Creating function to create patient
def create_patient(db: Session, id: UUID, patient_generalinfo: str,
                   dental_chart: str,
                   allergy_history: UUID, medical_history: str):
    db_patient = models.PatientTable(id=id,
                                     patient_generalinfo=patient_generalinfo,
                                     dental_chart=dental_chart,
                                     allergy_history=allergy_history,
                                     medical_history=medical_history)

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# Creating function to remove pationt using patientID
def remove_patient(db: Session, patient_id: UUID):
    _patient = get_patient_by_id(db=db, patient_id=patient_id)
    db.delete(_patient)
    db.commit()


# creating function to update patient Informaiton
def update_patient(db: Session, id: UUID,
                   patient_generalinfo: str, dental_chart: str,
                   allergy_history: UUID, medical_history: str):
    _patient = get_patient_by_id(db=db, id=id)
    _patient.id = id
    _patient.allergy_history = allergy_history
    _patient.patient_generalinfo = patient_generalinfo
    _patient.dental_chart = dental_chart
    _patient.medical_history = medical_history

    db.commit()
    db.refresh(_patient)
    return _patient


# creating crud for Patient_allergy

def get_patient_allergy(db: Session):
    return db.query(Patient_allergy).all()


# Creating funciton to get information of pain by pain_patient_map id
def get_patient_allergy_by_id(db: Session, id: UUID):
    return db.query(Patient_allergy).filter(Patient_allergy.id == id).first()


# Creating function to create pain_patient
def create_patient_allergy(db: Session, id: UUID,
                           allergies_id: UUID, specific_cause: str,
                           specific_organs: str, allergy_time: date):
    db_patient_allergy = models.Patient_allergy(id=id,
                                                allergies_id=allergies_id,
                                                specific_cause=specific_cause,
                                                specific_organs=specific_organs,
                                                allergy_time=allergy_time)

    db.add(db_patient_allergy)
    db.commit()
    db.refresh(db_patient_allergy)
    return db_patient_allergy

# Creating function to remove pain_patient using pain_patient id


def remove_patient_allergy(db: Session, id: UUID):
    _patient_allergy = get_patient_allergy_by_id(db=db, id=id)
    db.delete(_patient_allergy)
    db.commit()


# creating function to update patient_allergy Informaiton
def update_patient_allergy(db: Session, id: UUID,
                           allergies_id: UUID, specific_cause: str,
                           specific_organs: str, allergy_time: date):
    _patient_allergy = get_patient_allergy_by_id(db=db, id=id)
    # _patient_allergy.id = id
    _patient_allergy.allergies_id = allergies_id
    _patient_allergy.specific_cause = specific_cause
    _patient_allergy.specific_organs = specific_organs
    _patient_allergy.allergy_time = allergy_time

    db.commit()
    db.refresh(_patient_allergy)
    return _patient_allergy


# creating crud for allergies

def get_allergies(db: Session):
    return db.query(Allergies_class).all()


# Creating funciton to get information of pain by pain_patient_map id
def get_allergies_by_id(db: Session, id: UUID):
    return db.query(Allergies_class).filter(Allergies_class.id == id).first()


# Creating function to create allergies
def create_allergies(db: Session, id: UUID, id1: UUID, allergy_name: str,
                     allergy_organ: str, allergy_cause: str):
    db_allergies = models.Allergies_class(id=id,
                                          id1=id1,
                                          allergy_name=allergy_name,
                                          allergy_organ=allergy_organ,
                                          allergy_cause=allergy_cause)

    db.add(db_allergies)
    db.commit()
    db.refresh(db_allergies)
    return db_allergies


# Creating function to remove allergies using  id


def remove_allergies(db: Session, id: UUID):
    _allergies = get_allergies_by_id(db=db, id=id)
    db.delete(_allergies)
    db.commit()

# creating function to update pain_history Informaiton


def update_allergies(db: Session, id: UUID, id1: UUID,
                     allergy_name: str,
                     allergy_organ: str, allergy_cause: str):
    _allergies = get_allergies_by_id(db=db, id=id)
    _allergies.id = id
    _allergies.id1 = id1
    _allergies.allergy_name = allergy_name
    _allergies.allergy_organ = allergy_organ
    _allergies.allergy_cause = allergy_cause

    db.commit()
    db.refresh(_allergies)
    return _allergies
