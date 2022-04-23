from marshmallow import Schema, fields

from utils.database import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    address = db.relationship("Address")


class CompanySchema(Schema):
    class Meta:
        load_only = ("address_id",)

    id = fields.Integer()
    name = fields.String()
    address_id = fields.Integer()
    address = fields.Nested("AddressSchema", many=False)
