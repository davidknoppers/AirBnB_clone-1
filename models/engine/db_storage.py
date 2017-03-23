#!/usr/bin/python3
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__valid_classes = {"User": User,
                                   "Amenity": Amenity, "City": City,
                                   "Place": Place, "Review": Review,
                                   "State": State}

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_DB'),
            getenv('HBNB_MYSQL_ENV'))
        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = Session()
        if mysql_env == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        objects = {}
        if cls is None:
            for orm_key, orm_class in self.valid_classes.items():
                for instance in self.__session.query(orm_class):
                    objects[instance.id] = instance
        else:
            for instance in self.__session.query(cls):
                objects[instance.id] = instance
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = Session()
