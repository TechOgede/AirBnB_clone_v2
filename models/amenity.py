#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity,
                                   back_populates='amenities')
