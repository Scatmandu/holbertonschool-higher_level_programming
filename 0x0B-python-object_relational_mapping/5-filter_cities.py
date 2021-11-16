#!/usr/bin/python3

"""lists all states from the database hbtn_0e_0_usa"""


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

    cur.execute(
        "SELECT cities.name, states.name\
         FROM cities INNER JOIN states ON cities.state_id = states.id\
         ORDER BY cities.id ASC")
    rows = cur.fetchall()
    list_store = []
    for row in rows:
        if row[1] == argv[4]:
            list_store.append(row[0])
    string = ""
    for i, item in enumerate(list_store):
        if i < len(list_store) - 1:
            string += str(item) + ', '
        else:
            string += str(item)
    print(string)
    cur.close()
    db.close()
