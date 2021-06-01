#!/usr/bin/python3
"""displays values from database where name matches user input"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cursor = db.cursor()
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name = BINARY %(name)s
        """, {
                'name': argv[4]
        })
        results = cursor.fetchall()
    for item in results:
        print(item)
