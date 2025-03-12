#!/usr/bin/python3
"""Write a script that prints the first State object from the database hbtn_0e_6_usa"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State

if __name__ == "__main__":
    
    """ as in task 7 -- Base = declarative_base not needed to create table"""

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    port = 3306

    """not safe as detail parsed as string 
    url_object = URL.create(
        "mysql+mysqldb",
        username=mysql_username,
        password=mysql_password,
        host="localhost",
        port=3306,
        database=database_name)
    engine = create_engine(url_object)"
    """

    """ safer way """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(mysql_username, mysql_password, port, database_name),
                           pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()  # start a session

    first_state = session.query(State).limit(1).offset(0).one_or_none()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
