#!/usr/bin/python3.4
""" Displays all values in the states table where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
    WHERE states.name LIKE BINARY '{}'\
    ORDER BY states.id ASC".format(sys.argv[4]))

    query_rows = cursor.fetchall()

    for state in query_rows:
        print(state)

    cursor.close()
    db.close()
