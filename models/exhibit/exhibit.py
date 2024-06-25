from sqlalchemy import Column, String, DateTime, ForeignKey, inspect
from sqlalchemy.orm import relationship
from datetime import datetime

from models.interaction import Interaction
from database import Base

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Exhibit(Base):
    __tablename__ = 'exhibit'
# Auto Generated Fields:
    id           = Column(String(50), primary_key=True, nullable=False, unique=True)
    created      = Column(DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    name        = Column(String(100), nullable=False)
    introduction = Column(String(100), nullable=True)
    number       = Column(String(100), nullable=False)
    timeID       = Column(String(50), ForeignKey("time.id"), nullable=True)
    exhibitGroupID = Column(String(50), ForeignKey("exhibit_group.id"), nullable=True)
    
    interactions = relationship(Interaction.__name__, backref='exhibit')

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
