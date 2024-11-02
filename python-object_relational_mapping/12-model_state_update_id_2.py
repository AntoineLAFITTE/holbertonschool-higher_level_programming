#!/usr/bin/python3
"""
A script that changes the name of the State object with id = 2
to “New Mexico” in the database hbtn_0e_6_usa.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
./12-model_state_update_id_2.py
<mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306
and updates the name of the state with id = 2.
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

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name if the state is found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
