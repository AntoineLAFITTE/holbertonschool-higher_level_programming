#!/usr/bin/python3
"""
Defines a State class and creates an instance of Base from SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that links to the 'states' table in MySQL database
    Attributes:
    id (int): The state's id, auto-generated, unique, primary key, not null
    name (str): The state's name, string with max 128 characters, not null
    """
    #  This is the link to MySql table called states.
    __tablename__ = 'states'
    # Columns :
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
