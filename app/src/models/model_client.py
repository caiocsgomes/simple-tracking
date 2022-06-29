from typing import List

from marshmallow import Schema, fields, post_load

from models.model_address import AddressSchema, Address
from utils.database import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.relationship("Address")

    def __init__(self, name: str, email: str, address: List[Address]):
        self.name = name
        self.email = email
        self.address = address

    def __repr__(self):
        return f"Client({self.name}, {self.email}, {self.address_id})"

    def __getitem__(self, item):
        return getattr(self, item)


class ClientSchema(Schema):
    class Meta:
        load_only = ('address_id',)

    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    address = fields.Nested(AddressSchema, many=True)

    @post_load
    def make_client(self, data, **kwargs):
        return Client(**data)
