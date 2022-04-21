from marshmallow import Schema, fields, post_load

from utils.database import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def __init__(self, name: str, email: str, address_id: int):
        self.name = name
        self.email = email
        self.address_id = address_id

    def __repr__(self):
        return f"Client({self.name}, {self.email}, {self.address_id})"


class ClientSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    address_id = fields.Int()

    @post_load
    def make_client(self, data, **kwargs):
        return Client(**data)
