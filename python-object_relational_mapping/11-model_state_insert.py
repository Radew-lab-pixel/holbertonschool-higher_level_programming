#!/usr/bin/python3
"""Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    port = 3306
    state_to_add = "Louisiana"

    # Base = declarative_base()  not needed as table already exists

    # create core engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(mysql_username, mysql_password, port,
                                   database_name), pool_pre_ping=True)

    # start ORM engine (don't ask why, just follow the procedure:< )
    Session = sessionmaker(bind=engine)
    session = Session()  # start a session

    # create an new entry object from State class
    new_entry = State(name=state_to_add)

    # adding entry like git add. & git commit -m
    session.add(new_entry)  # add entry to table
    session.commit()  # save to database

    # Read/ query
    # results = session.query(State).order_by(State.id).all()  for debugging
    """results = session.query(State).all().order_by(State.id)
    error as have to be in sequence """
    results = session.query(State).filter(
        State.name == state_to_add).order_by(State.id).all()

    """ for debugging purpose
    for result in results:
        print(f"{result.id}: {result.name}")
    """
    for result in results:
        print(f"{result.id}")

    # optional but good practice to prevent leaks if any error for security
    session.close()
