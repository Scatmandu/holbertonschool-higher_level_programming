#!/usr/bin/python3

"""lists all cities and states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=password,
                         db=database,
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities, states \
                WHERE states.id = state_id \
                GROUP BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
