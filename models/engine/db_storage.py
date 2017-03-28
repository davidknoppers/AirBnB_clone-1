#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place, PlaceAmenity
from models.review import Review
from models.state import State

from os import getenv, environ


class DBstorage:
    __engine = None
    __session = None

    valid_classes = {"User": User,
                     "Amenity": Amenity, "City": City,
                     "Place": Place, "Review": Review,
                     "State": State}

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')))

        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = Session()
        try:
            if environ['HBNB_MYSQL_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except:
            pass

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
            eval(obj).query.filter_by(id=obj.id).delete()

    def reload(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')))

        self.__session = scoped_session(sessionmaker(bind=self.__engine))
    def close(self):
        """
        simply calls remove on the session
        """
        self.remove(self.__session)
