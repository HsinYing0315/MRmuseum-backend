from sqlalchemy import inspect
from datetime import datetime

from __init__ import db # from __init__.py

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Questionnaire(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    interactionScore    = db.Column(db.Integer, nullable=True)
    educationScore      = db.Column(db.Integer, nullable=True)
    entertainmentScore  = db.Column(db.Integer, nullable=True)
    overallScore        = db.Column(db.Integer, nullable=True)
    willVisitAgain      = db.Column(db.Boolean, nullable=True)
    visitorID = db.Column(db.String(50), db.ForeignKey("visitor.id"), nullable=False)

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
