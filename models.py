from sqlalchemy import (Column, Date, Float, Integer, Boolean, ForeignKey,
                        String, DateTime)
from sqlalchemy.dialects.postgresql import UUID
from config import Base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType
from datetime import datetime


# This class holds user_basic informations
class UserTable(Base):
    __tablename__ = 'user_basic'
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    profile_pic = Column(URLType)
    is_verified = Column(Boolean)
    auth_provider = Column(String(255))
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # Rel1 = relationship("PatientTable",  back_populates="Rel2")

    # patient_info = relationship("PatientTable", back_populates="users")


# This class holds patient informations
class PatientTable(Base):
    __tablename__ = 'patient_info'
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    patient_generalinfo = Column(String)
    dental_chart = Column(String)
    allergy_history = Column(UUID(as_uuid=True),
                             ForeignKey('patient_allergy_map.id',
                             ondelete='CASCADE'))
    medical_history = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    Rel3 = relationship("Patient_allergy", back_populates="Rel4")


class Patient_allergy(Base):
    __tablename__ = "patient_allergy_map"
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    allergies_id = Column(UUID(as_uuid=True), primary_key=True)
    specific_cause = Column(String)
    specific_organs = Column(String)
    allergy_time = Column(DateTime)
    
    Rel4 = relationship("PatientTable", back_populates="Rel3")
    Rel5 = relationship("Allergies_class", back_populates="Rel6")


# holds the alergies information


class Allergies_class(Base):
    __tablename__ = "allergies"
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    id1 = Column(UUID(as_uuid=True),
                 ForeignKey('patient_allergy_map.allergies_id',
                            ondelete='CASCADE'))
    allergy_name = Column(String)
    allergy_organ = Column(String)
    allergy_cause = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    Rel6 = relationship("Patient_allergy", back_populates="Rel5")
