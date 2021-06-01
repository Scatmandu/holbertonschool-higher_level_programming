#!/usr/bin/python3
"""lists city ids, city names, and state names from database"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3],)
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                states
            JOIN
                cities
            ON
                states.id = cities.state_id
            """)
        data = cursor.fetchall()
    for item in data:
        print(item)
