from dataclasses import dataclass

from marshmallow import Schema, fields, post_load

from utils.database import db


# TODO: Decouple model from sqlalquemy
# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html

@dataclass
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(20), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    address_type = db.Column(db.String(10), nullable=True)
    # RULE: only one address can be preferred
    # TODO: add partial index to preferred
    # https://stackoverflow.com/questions/27976683/creating-partial-unique-index-with-sqlalchemy-on-postgres
    # https://stackoverflow.com/questions/59691425/how-to-enforce-that-there-is-only-one-true-value-in-a-column-per-names-in-an
    # preferred = db.Column(db.Bool, nullable=False, default=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    def __getitem__(self, item):
        return getattr(self, item)


class AddressSchema(Schema):
    id = fields.Int()
    street = fields.Str()
    number = fields.Int()
    postal_code = fields.Str()
    city = fields.Str()
    state = fields.Str()
    address_type = fields.Str()
    client_id = fields.Int()

    @post_load
    def make_address(self, data, **kwargs):
        return Address(**data)
