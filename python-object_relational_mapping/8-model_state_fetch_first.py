#!/usr/bin/python3
"""
This script prints the first State object or 'Nothing' if table is empty.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

"""
Takes 3 arguments: username, password, database name
Prints the first State by id
"""

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    if first:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")
