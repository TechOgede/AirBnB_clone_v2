#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from models.place import place_amenity
import os


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary=place_amenity,
                                       back_populates='amenities')
