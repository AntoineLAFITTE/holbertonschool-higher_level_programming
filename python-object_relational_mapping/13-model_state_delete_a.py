#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306
and deletes all states containing the letter 'a' in their name.
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

    # Query all State objects containing 'a' in their name
    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    # Delete each state in the result set
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to apply changes
    session.commit()

    # Close the session
    session.close()
