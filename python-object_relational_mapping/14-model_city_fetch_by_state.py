#!/usr/bin/python3
""" Write a script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State
from model_city import City
 
if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    port = 3306

    # create core engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(mysql_username, mysql_password, port,
                                   database_name), pool_pre_ping=True)
    # start ORM engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # SELECT * FROM State JOIN City WHERE State.id = City.state_id
    # thus session.query(State, City) like FROM State Join City
    # .filter(State.id == City.state_id) like WHERE State.id = City.state_id
    # .all is SELECT *
    results = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    # for result in results:

    # can access state and city in results as session.query
    # return both tables structure
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()  # optional close for security
