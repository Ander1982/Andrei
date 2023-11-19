from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = "dz_39.db"

engine = create_engine(f"sqlite:///{DATABASE_NAME}")

Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db1():
    Base.metadata.create_all(engine)
