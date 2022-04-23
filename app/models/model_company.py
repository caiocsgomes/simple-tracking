from marshmallow import Schema

from utils.database import db


class Company(db.Model):
    pass


class CommanySchema(Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'phone', 'email', 'website', 'logo', 'created_at', 'updated_at')
