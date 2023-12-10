#!/usr/bin/python3
"""Module representation of class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class implementation of object Place

    Attributes:
        city_id (str): the id of a city
        user_id (str): the user id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum guests in place
        price_by_night (int): price per night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list): list of amenity ids
    """

    city = ""
    user_id = ""
    name = ""
    desctription = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
