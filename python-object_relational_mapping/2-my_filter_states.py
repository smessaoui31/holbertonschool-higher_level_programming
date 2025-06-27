#!/usr/bin/python3
"""
This script prints states with a name equal to the argument (unsafe).
"""
import MySQLdb
import sys

"""
Takes 4 arguments: username, password, database name, state name
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
    query = "SELECT * FROM states WHERE name =" \
            " '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
