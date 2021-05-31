#!/usr/bin/python3
"""lists all states from selected database"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for state in result:
        if state[1][0] == "N":
            print(state)
