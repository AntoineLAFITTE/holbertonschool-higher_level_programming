#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database hbtn_0e_4_usa.

The script takes four arguments:
1. MySQL username
2. MySQL password
3. Database name
4. State name to filter by

Usage:
    ./5-filter_cities.py
      <mysql_username> <mysql_password> <database_name> <state_name>

The script connects to a MySQL server running on localhost at port 3306
and retrieves cities of the specified state,
sorted by cities.id in ascending order.
The output is a single line with the city names separated by commas.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # SQL query to retrieve cities of the specified state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all results and format as a comma-separated list
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
