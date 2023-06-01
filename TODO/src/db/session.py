from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


def create_session():
    db_name = "Task.db"
    db_engine = create_engine(f"sqlite:///db/{db_name}")

    return Session(db_engine)

def init():
    db_name = "Task.db"
    db_engine = create_engine(f"sqlite:///db/{db_name}") #connection string
    #Base.metadata.drop_all(db_engine) # ovo brise sve nije dobra praxa
    Base.metadata.create_all(db_engine) #dali create all ako nema 16 kreira bazu s duplim tablicama

    return Session(db_engine)
