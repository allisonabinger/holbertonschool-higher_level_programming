#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys


def list_all_states(username, password, db_name, host, port):

    """ Listing states in db """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=db_name,
        host=host,
        port=port
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    list_all_states(username, password, db_name, host, port)
