#!/usr/bin/python3
"""
This script prints the id of a State with a given name.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

"""
Takes 4 arguments: username, password, database name, state name
Prints the id if found, else 'Not found'
"""

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
