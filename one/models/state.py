#!/usr/bin/python3
'''This module creates a User class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''The class for managing state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''It initializes attributes for the State class'''
        super().__init__(*args, **kwargs)
