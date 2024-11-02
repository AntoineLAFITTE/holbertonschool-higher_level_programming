#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306,
adds the new state “Louisiana” to the states table,
and prints the id of the new state.
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

    # Create a new State object for "Louisiana" and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new state
    print(new_state.id)

    # Close the session
    session.close()
