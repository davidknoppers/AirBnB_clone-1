#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Table, Column, String
from os import getenv
from sqlalchemy.orm import relationship

class City(BaseModel):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
