from flask_sqlalchemy import SQLAlchemy
from models.model_address import Address
from models.model_company import Company
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table
from sqlalchemy.orm import registry, relationship
from src.models.model_client import Client


class SqlAlquemyDb:

    def __int__(self, uri):
        """
        Initializes the engine, which is the connector between the app and the specified DB.
        docs: https://docs.sqlalchemy.org/en/14/orm/quickstart.html

        :param uri: conn string in the format dialect+driver://username:password@host:port/database
        """
        self.engine = create_engine(uri)
        self.metadata = MetaData()

    def init_db(self):
        """
        Initializes the db, assigning the db schema to the metadata.
        The metadata is the sqlalquemy object that holds data about our schema (tables, relationships, indexes, etc)

        :return: None
        """
        self.start_mappers()

    def start_mappers(self):
        mapper_registry = registry(metadata=self.metadata)

        client = Table('client', self.metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String, nullable=False),
                       Column('email', String, nullable=False),
                       Column('address_id', Integer, nullable=True),
                       Column('company_id', Integer, nullable=True)
                       )
        mapper_registry.map_imperatively(Client, client, properties={
            'address': relationship(Address, backref='user'),
            'company': relationship(Company)
        })
        mapper_registry.map_imperatively(Client, client)
