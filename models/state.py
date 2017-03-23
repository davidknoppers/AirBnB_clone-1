#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column, String
from sqlalchemy.orm import relationship, backref
from os import getenvfrom models import *


class State(BaseModel):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
