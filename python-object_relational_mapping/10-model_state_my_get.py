#!/usr/bin/python3
"""
A script that prints the State object's id with the name passed as an argument
from the database hbtn_0e_6_usa.

The script takes four arguments:
1. MySQL username
2. MySQL password
3. Database name
4. State name to search for

Usage:
./10-model_state_my_get.py
<mysql_username> <mysql_password> <database_name> <state_name>

The script connects to a MySQL server running on localhost at port 3306
and displays the id of the state with the given name.
If not found, it prints 'Not found'.
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
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
