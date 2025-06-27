#!/usr/bin/python3
"""
This module defines the City class to map to the table 'cities'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

# City class inherits from Base and links to states
class City(Base):
    """
    City class with id, name, and state_id columns.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
