#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
./14-model_city_fetch_by_state.py
<mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306
and displays each city along with its associated state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, joined with State, ordered by cities.id
    results = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    # Display results
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close the session
    session.close()
