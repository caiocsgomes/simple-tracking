from models.model_address import Address
from repository.repository_base import AbstractRepository
from utils.database import db
from utils.exceptions import NotFoundException


class DefaultRepository(AbstractRepository):
    entity: db.Model

    def __init__(self, entity):
        self.entity = entity

    def get_by_id(self, id: int) -> db.Model:
        obj = self.entity.query.get(id)
        if obj is None:
            raise NotFoundException("Entity not found")
        return obj

    def create(self, obj: db.Model) -> db.Model:
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, id: int, new_obj: db.Model) -> db.Model:
        obj = Address.query.get(id)
        if obj is None:
            raise NotFoundException("Address not found")
        new_address_keys = [x for x in vars(new_obj) if not x.startswith('_')]
        for key in new_address_keys:
            if new_obj[key] != obj[key]:
                setattr(obj, key, new_obj[key])
        db.session.commit()
        return obj

    def delete(self, id: int) -> db.Model:
        obj = self.entity.query.get(id)
        if obj is None:
            raise NotFoundException("Address not found")
        db.session.delete(obj)
        db.session.commit()
        return obj
