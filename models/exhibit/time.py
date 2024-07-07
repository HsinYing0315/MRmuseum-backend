from sqlalchemy import Column, String, DateTime, ForeignKey, inspect
from sqlalchemy.orm import relationship
from datetime import datetime

from models.exhibit.exhibitGroup import ExhibitGroup
from models.exhibit.exhibit import Exhibit

from database import Base

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Time(Base):
    __tablename__ = 'time'
# Auto Generated Fields:
    id           = Column(String(50), primary_key=True, nullable=False, unique=True)
    created      = Column(DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    name        = Column(String(100), nullable=False)
    location     = Column(String(100), nullable=False)
    introduction = Column(String(3000), nullable=True)
    areaID       = Column(String(50), ForeignKey("area.id"), nullable=False)

    exhibitGroups = relationship(ExhibitGroup.__name__, backref='time')
    exhibits     = relationship(Exhibit.__name__, backref='time')

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
