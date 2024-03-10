#!/usr/bin/python3
'''This module creates a User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''The class for managing user objects'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''It initializes attributes for the User class'''
        super().__init__(*args, **kwargs)
