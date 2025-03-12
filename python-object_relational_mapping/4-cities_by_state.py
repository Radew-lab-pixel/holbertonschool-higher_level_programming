#!/usr/bin/python3
""" Write a script that lists all cities
    from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # establish a connection
   

    # cursor pointer
    pointer = db.cursor()

    # execute a query
    pointer.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON cities.state_id = states.id")

    # fetch result from pointer
    rows = pointer.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")

    # close pointer and db
    pointer.close()
    db.close()
