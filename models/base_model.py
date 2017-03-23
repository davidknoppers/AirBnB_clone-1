#!/usr/bin/python3
from datetime import datetime
import uuid
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The base class for all objects"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(), default=datetime.now(), nullable=False)
        updated_at = Column(DateTime(), default=datetime.now(), nullable=False,
                            onupdate=datetime.now())

    def __init__(self, *args, **kwargs):
        """make a class object"""
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            if len(args) > 0:
                for k in args[0]:
                    setattr(self, k, args[0][k])

        for key, val in kwargs.items():
            setattr(self, key, val)

        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
        else:
            if not hasattr(self, 'created_at'):
                self.created_at = datetime.now()
            if not hasattr(self, 'id'):
                self.id = str(uuid.uuid4())

    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe
    def delete(self):
        models.storage.delete(self.id)
