from application.db import db
from sqlalchemy import DateTime, func


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(DateTime, nullable=False, default=func.now())
    updated = db.Column(DateTime, default=func.now(), onupdate=func.now())
