#!/usr/bin/python3
""" Write a script that changes the name of a State
    object from the database hbtn_0e_6_usa
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
    port = 3306
    state_id_search = 2
    replaced_name = "New Mexico"

    # create core engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(mysql_username, mysql_password, port,
                                   database_name), pool_pre_ping=True)

    # start ORM engine
    Session = sessionmaker(bind=engine)
    session = Session()  # start session

    # filter for the State object of id = 2 that needed update
    results = session.query(State).filter(State.id == state_id_search).all()

    # update name
    for result in results:
        result.name = replaced_name
        session.commit()  # apply update change

    session.close()  # good practice to close session for security
