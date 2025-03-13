#!/usr/bin/python3
""" Write a script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
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
    search_char = '%a%'

    # create core engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(mysql_username, mysql_password, port,
                                   database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)  # start ORM engine
    session = Session()  # start session

    # Filter for State object of name containing 'a'

    # == doesn't work as not deleting
    # results = session.query(State).filter(State.name == search_char).all()

    results = session.query(State).filter(State.name.like(search_char)).all()

    for result in results:
        session.delete(result) # has to delete one object or data one at a time
    session.commit()  # apply delete change to database

    session.close()
