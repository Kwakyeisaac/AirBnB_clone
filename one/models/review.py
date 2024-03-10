#!/usr/bin/python3
'''This module creates a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''The class for managing review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''It initializes attributes for the review class'''
        super().__init__(*args, **kwargs)
