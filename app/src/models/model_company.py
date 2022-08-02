from marshmallow import Schema, fields, post_load
from models.model_address import Address


class Company:
    id: int
    name: str
    address: Address

    def __getitem__(self, item):
        return getattr(self, item)


class CompanySchema(Schema):
    class Meta:
        load_only = ("address_id",)

    id = fields.Integer()
    name = fields.String()
    address_id = fields.Integer()
    address = fields.Nested("AddressSchema", many=False)

    @post_load
    def make_client(self, data, **kwargs):
        return Company(**data)
