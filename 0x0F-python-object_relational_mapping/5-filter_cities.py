#!/usr/bin/python3.4
""" Take in the name of a state and list all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states\
    ON states.id = cities.state_id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (sys.argv[4],))

    states_cities = cursor.fetchall()

    cities = []

    for city in states_cities:
        cities.append(city[1])

    cities = ", ".join(cities)
    print(cities)

    cursor.close()
    db.close()
