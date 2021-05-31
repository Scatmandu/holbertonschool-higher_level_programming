#!/usr/bin/python3
"""
lists states from database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for state in result:
        print(state)
