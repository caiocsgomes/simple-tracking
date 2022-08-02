from dataclasses import dataclass

from marshmallow import Schema, fields, post_load

from models.model_address import AddressSchema, Address


@dataclass
class Client:
    id: int
    name: str
    email: str
    address: Address

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
