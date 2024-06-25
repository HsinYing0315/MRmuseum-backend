from sqlalchemy import Column, String, DateTime, ForeignKey, relationship, inspect
from datetime import datetime

from models.exhibit.exhibit import Exhibit
from database import Base

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class ExhibitGroup(Base):
# Auto Generated Fields:
    id           = Column(String(50), primary_key=True, nullable=False, unique=True)
    created      = Column(DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    timeID       = Column(String(50), ForeignKey("time.id"), nullable=False)

    exhibits     = relationship(Exhibit.__name__, backref='exhibitGroup')

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
