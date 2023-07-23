#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import *
from sqlalchemy import Float


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False,
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False,
                             primary_key=True),
                      mysql_collate='latin1_swedish_ci'
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship('Review', cascade='all, delete-orphan',
                           backref='place')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False,
                             back_populates='place_amenities')

    amenity_ids = []

    @property
    def reviews(self):
        ''' Relationship for File Storage'''
        reviews = []
        all_reviews = storage.all(Review)
        for value in all_reviews.values():
            if value.place_id == self.id:
                reviews.append(value)

        return reviews

    @property
    def amenities(self):
        ''' Relationship for File Storage'''
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        ''' Setter that handles append method '''
        if obj.__class__.__name__ == 'Amenity':
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
