from marshmallow import Schema, fields, post_load

from utils.database import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    address = db.relationship("Address")

    def __init__(self, name, address_id):
        self.name = name
        self.address_id = address_id

    def __repr__(self):
        return f"Company('{self.name}', '{self.address_id}')"

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
