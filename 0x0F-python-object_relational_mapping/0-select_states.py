#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb

# Connect to the hbtn_0e_0_usa database
conn = mysqldb.connect(database="hbtn_0e_0_usa", user="root", password="root", host="localhost", port="3306")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute the SELECT statement to retrieve all states from the states table
cur.execute("SELECT name FROM states")

# Fetch all the results
results = cur.fetchall()

# Iterate through the results and print out the name of each state
for row in results:
    print(row[0])

# Close the cursor and database connection
cur.close()
conn.close()
