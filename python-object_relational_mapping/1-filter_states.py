#!/usr/bin/python3
"""
This script prints states starting with 'N' from the database.
"""
import MySQLdb
import sys

"""
Takes 3 arguments: username, password, database name
Prints states where name starts with 'N'
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
