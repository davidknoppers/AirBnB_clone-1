#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class User(BaseModel):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
