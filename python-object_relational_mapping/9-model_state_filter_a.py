#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
that contain the letter 'a' in their name.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306
and lists all states containing 'a' in ascending order by states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Query all State objects containing 'a' and order by id
    states_with_a = (
    session.query(State)
    .filter(State.name.like('%a%'))
    .order_by(State.id)
    .all()
    )

    # Print each state's id and name
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
