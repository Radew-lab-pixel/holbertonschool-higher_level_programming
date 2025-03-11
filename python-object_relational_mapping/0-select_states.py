#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa: """
import MySQLdb
import sys

def main():
    # read argumnent
    n = len(sys.argv)
    """if n != 3:
    print("Arguments number need to be 3")
    exit()
    """
    mysql_username = sys.argv[0]
    mysql_password = sys.argv[1]
    database_name = sys.argv[2]
    # Establish a connection
    db = MySQLdb.connect(host="localhost", port=3306,
        user=mysql_username, password=mysql_password, database=database_name)

    # create a cursor pointer
    pointer = db.cursor()

    # execute a query
    pointer.execute("SELECT * FROM states ORDER BY id")

    # fetch the result (fetchone fetch the next row)
    row = pointer.fetchone()
    while row is not None:
        print(row)
        row = pointer.fetchone()

    # close cursor pointer and db connection
    pointer.close()
    db.close()

if __name == "__main__":
    sys.exit(main())
