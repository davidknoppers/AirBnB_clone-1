#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column, String
from os import getenv


class Amenity(BaseModel):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
