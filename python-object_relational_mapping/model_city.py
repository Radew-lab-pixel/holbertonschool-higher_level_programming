# from model_city import State  -- translation error not needed
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # instance base

#class inherited from Base
class City(Base):
    """  
    City class:
    argument -- Base declarative
    Return: None
    """
    # table mapping to MYSQL table
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))  # not foreign_key , why ??
