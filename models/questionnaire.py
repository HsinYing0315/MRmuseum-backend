from sqlalchemy import Column, String, DateTime, Integer, Boolean, ForeignKey, inspect
from datetime import datetime

from database import Base

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Questionnaire(Base):
    __tablename__ = 'questionnaire'
# Auto Generated Fields:
    id           = Column(String(50), primary_key=True, nullable=False, unique=True)
    created      = Column(DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    interactionScore    = Column(Integer, nullable=True)
    educationScore      = Column(Integer, nullable=True)
    entertainmentScore  = Column(Integer, nullable=True)
    overallScore        = Column(Integer, nullable=True)
    willVisitAgain      = Column(Boolean, nullable=True)
    visitorID = Column(String(50), ForeignKey("visitor.id"), nullable=False)

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
