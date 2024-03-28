from sqlalchemy import inspect
from datetime import datetime

from .. import db # from __init__.py

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Interaction(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    question        = db.Column(db.String(100), nullable=False)
    visitorID       = db.Column(db.String(50), db.ForeignKey("visitor.id"), nullable=False)
    exhibitID       = db.Column(db.String(50), db.ForeignKey("exhibit.id"), nullable=False)

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
