#!/usr/bin/python3
""" Write a script that lists all State objects
    that contain the letter a from the database hbtn_0e_6_usa
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format
                           (mysql_username, mysql_password, port,
                            database_name), pool_pre_ping=True)

    # start ORM engine
    Session = sessionmaker(bind=engine)
    session = Session()  # start a session

    results = session.query(
        State).filter(State.name.like('%a%')).order_by(State.id)

    for result in results:
        print(f"{result.id}: {result.name}")
