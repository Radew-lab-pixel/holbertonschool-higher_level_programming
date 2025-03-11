#!/usr/bin/python3
""" Write a script that lists all cities by states
    from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    # Check for correct number of arguments - recommended by chat
    if len(sys.argv) != 5:
        print("Usage: ./script.py <user> <pass> <db> <state>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # establish a connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         password=mysql_password,
                         database=database_name)

    # cursor pointer
    pointer = db.cursor()

    # execute a query
    pointer.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                        WHERE binary states.name = %s\
                    ORDER BY cities.id", (state_name,))

    # fetch result from pointer
    rows = pointer.fetchall()
    if rows:

        """
        n = len(rows)
        count = 0  # counter for detecting last row
        for row in rows:
            if count != (n-1):
                print(f"{row[0]},", end=" ")
            else:
                print(f"{row[0]}")
            count += 1"
        """
        # recommended by chatGPT to pass the checker on NULL cities
        cities = [row[0] for row in rows]
        print(", ".join(cities))

    # print()
    # close pointer and db
    pointer.close()
    db.close()
