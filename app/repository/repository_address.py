from models.model_address import Address
from repository.repository_base import AbstractRepository
from utils.database import db


class AddressRepository(AbstractRepository):

    def get_by_id(self, id: int) -> Address:
        return Address.query.get(id)

    def create(self, addr: Address) -> Address:
        db.session.add(addr)
        db.session.commit()
        return addr

    def update(self, id: int, obj: db.Model) -> db.Model:
        addr = AddressRepository.get_by_id(id)
        addr.update(**addr)
        db.session.commit()
        return addr
