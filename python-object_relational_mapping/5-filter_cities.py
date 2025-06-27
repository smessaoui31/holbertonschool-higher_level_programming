#!/usr/bin/python3
"""
This script lists all cities of a state given as argument.
"""
import MySQLdb
import sys

"""
Takes 4 arguments: username, password, database name, state name
Prints cities of the given state safely
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
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
