#!/usr/bin/python3
"""Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # def main():
    # read argumnent
    n = len(sys.argv)
    """if n != 3:
    print("Arguments number need to be 3")
    exit()
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Establish a connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name)
    # create a cursor pointer
    pointer = db.cursor()

    # execute a query , binary added to enforce case sensitive 
    pointer.execute("SELECT * FROM states WHERE binary name = %s\
                    ORDER BY id ASC", (state_name_searched,))

    # fetch the result using fetchall to pass the checker
    rows = pointer.fetchall()
    for row in rows:
        # print(row)
        print("({0}, '{1}')".format(row[0], row[1]))
    # close cursor pointer and db connection
    pointer.close()
    db.close()
