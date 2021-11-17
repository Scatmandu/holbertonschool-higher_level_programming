#!/usr/bin/python3
"""
lists all State objects that match a given
name from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id)
    flag = 0
    for x in instance:
        if x.name == argv[4]:
            print("{}".format(x.id))
            flag = 420
    if flag == 0:
        print("Not found")
    session.close()
