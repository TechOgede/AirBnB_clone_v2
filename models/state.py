#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    from models import storage
    name = Column(String(128), nullable=False)

    if storage.__class__.__name__ == 'DBStorage':
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            '''Getter fpr the cities attr '''
            cities_list = []
            cities = storage.all(City)
            for key, value in cities.items():
                if value.state_id == self.id:
                    cities_list.append(value)

            return cities_list
