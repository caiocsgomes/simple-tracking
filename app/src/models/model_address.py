from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class Address:
    id: int
    street: str
    number: int
    postal_code: str
    city: str
    state: str
    address_type: str
    preferred: bool
    # RULE: only one address can be preferred
    # TODO: add partial index to preferred
    # https://stackoverflow.com/questions/27976683/creating-partial-unique-index-with-sqlalchemy-on-postgres
    # https://stackoverflow.com/questions/59691425/how-to-enforce-that-there-is-only-one-true-value-in-a-column-per-names-in-an
    # preferred = db.Column(db.Bool, nullable=False, default=False)

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
