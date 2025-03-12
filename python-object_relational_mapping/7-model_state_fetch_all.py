#!/usr/bin/python3
"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State

if __name__ == "__main__":
    # instance base from Declarative base
    # Base = declarative_base()  # only for creating table thus
    # not needed as table been created 

    # class inherited from Base
    # class State(Base):  imported from model_state

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    # state_name = sys.argv[4]

    url_object = URL.create(
        "mysql+mysqldb",
        username=mysql_username,
        password=mysql_password,  # plain (unescaped) text
        host="localhost",
        port=3306,
        database=database_name)

    engine = create_engine(url_object)

    # sessionmaker replaced both Base.metadata.create_all(engine)
    # and session = Session(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        # print("{}: {}".format(state.id, state.name))
        print(f"{state.id}: {state.name}")
