from app.utils.database import db
from marshmallow import Schema, fields, post_load


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(20), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    address_type = db.Column(db.String(10), nullable=True)

    def __init__(self, street, number, postal_code, city, state, address_type):
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.address_type = address_type

    def __repr__(self):
        return f"Address({self.street}, {self.number} - {self.city}/{self.state})"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class AddressSchema(Schema):
    street = fields.Str()
    number = fields.Int()
    postal_code = fields.Str()
    city = fields.Str()
    state = fields.Str()
    address_type = fields.Str()

    @post_load
    def make_address(self, data, **kwargs):
        return Address(**data)
