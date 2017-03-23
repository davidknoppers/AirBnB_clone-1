#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, String, Integer, Float, Table, Column
from os import getenv


class State(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
