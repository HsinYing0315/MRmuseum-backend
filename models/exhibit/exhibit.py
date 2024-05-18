from sqlalchemy import inspect
from datetime import datetime

from models.interaction import Interaction
from __init__ import db # from __init__.py

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Exhibit(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    name        = db.Column(db.String(100), nullable=False)
    introduction = db.Column(db.String(100), nullable=True)
    number       = db.Column(db.String(100), nullable=False)
    timeID       = db.Column(db.String(50), db.ForeignKey("time.id"), nullable=True)
    exhibitGroupID = db.Column(db.String(50), db.ForeignKey("exhibit_group.id"), nullable=True)
    
    interactions = db.relationship(Interaction.__name__, backref='exhibit')

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
