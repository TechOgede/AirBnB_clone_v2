#!/usr/bin/python3
''' This module defines the Database storage engine '''


import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    ''' This class defines the Database storage object '''
    __engine = None
    __session = None

    def __init__(self):
        ''' Initialises instance attrs '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' Return all types of objects or only objects of type "cls"
            from the database
        '''
        _objs = {}

        if cls:
            objs_list = self.__session.query(cls)
            for obj in objs_list:
                key = f'{obj.__class__.__name__}.{obj.id}'
                _objs[key] = obj

        else:
            tables = [User, State, City, Amenity, Place, Review]
            for table in tables:
                objs_list = self.__session.query(table)
                for obj in objs_list:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    _objs[key] = obj

        return _objs

    def new(self, obj):
        ''' Adds the object to the current database session '''
        self.__session.add(obj)

    def save(self):
        ''' Commits all changes of the current database session '''
        self.__session.commit()

    def delete(self, obj=None):
        ''' Deletes from the current database session'''
        if obj:
            self.__session.delete(obj, synchronize_session=False)

    def reload(self):
        '''Creates all tables in the database and creates the current
           database session
        '''
        Base.metadata.create_all(self.__engine)
        sesh_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh_fact)
        self.__session = Session()

    def close(self):
        ''' Remove current session '''
        self.__session.close()
