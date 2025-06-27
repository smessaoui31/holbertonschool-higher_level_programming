#!/usr/bin/python3
"""
This script lists all cities with their state names.
"""
import MySQLdb
import sys

"""
Takes 3 arguments: username, password, database name
Prints cities joined with their states sorted by city id
"""

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
