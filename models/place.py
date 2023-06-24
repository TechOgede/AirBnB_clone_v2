#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import *
from sqlalchemy import Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), default='N/A')
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, default='N/A')
    longitude = Column(Float, default='N/A')
    reviews = relationship('Review', cascade='all', backref='place')

    @property
    def reviews(self):
        ''' Relationship for File Storage'''
        reviews = []
        all_reviews = storage.all(Review)
        for value in all_reviews.values():
            if value.place_id == self.id:
                reviews.append(value)

        return reviews
