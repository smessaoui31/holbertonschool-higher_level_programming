#!/usr/bin/python3
"""
This script prints all City objects with their State names.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys

"""
Takes 3 arguments: username, password, database name
Prints cities ordered by id in the format: State: (id) City
"""

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State).order_by(City.id)
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
