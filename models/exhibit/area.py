from sqlalchemy import Column, String, DateTime, inspect
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base
from models.exhibit.time import Time

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Area(Base):
    __tablename__ = "area"
# Auto Generated Fields:
    id           = Column(String(50), primary_key=True, nullable=False, unique=True)
    created      = Column(DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    name        = Column(String(100), nullable=False)
    location     = Column(String(100), nullable=False)
    introduction = Column(String(3000), nullable=True)

    times        = relationship(Time.__name__, backref='area')
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
