#!/usr/bin/python3
"""
Defines a City class that links to the MySQL table `cities`.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that links to the `cities` table in the MySQL database.

    Attributes:
        id (int): The city's id, auto-generated,unique, primary key, not null.
        name (str): The city's name, string with max 128 characters, not null.
        state_id (int): The id of the associated state,
        foreign key to `states.id`, not null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
