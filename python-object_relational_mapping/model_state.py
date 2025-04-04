#!/usr/bin/python3
"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# instance base from Declarative base
Base = declarative_base()

# class inherited from Base


class State(Base):
    """ State class

        Attributes:
        Base : declarative base
    """
    # table mapping
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
