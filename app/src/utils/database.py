from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table

db = SQLAlchemy()

engine = None


def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine


def init_db():
    metadata = MetaData()

    client = Table('client', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String, nullable=False),
                   Column('email', String, nullable=False),
                   )

    ## TODO: Study relationship
