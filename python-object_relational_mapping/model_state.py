#!/usr/bin/python3
"""
This module defines the State class for SQLAlchemy.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""
Base class for ORM
"""

Base = declarative_base()


class State(Base):
    """
    State class with id and name columns.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
