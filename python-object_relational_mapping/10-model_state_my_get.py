#!/usr/bin/python3
""" Write a script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
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
    state_name_to_search = sys.argv[4]
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format
                           (mysql_username, mysql_password, port,
                            database_name), pool_pre_ping=True)

    # start ORM engine
    Session = sessionmaker(bind=engine)
    session = Session()  # start a session

    """ will not work as won't return a NULL if not matching"
        thus "Not found" won't be printed
    results = session.query(State).filter(
        State.name.like(state_name_to_search))
    """

    # filter is like WHERE in mySQL
    results = session.query(State).filter(
        State.name == state_name_to_search).all()

    if results:
        for result in results:
            print(f"{result.id}")
    else:
        print("Not found")
