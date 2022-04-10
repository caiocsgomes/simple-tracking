from models.model_address import Address
from repository.repository_base import AbstractRepository
from utils.database import db
from utils.exceptions import NotFoundException


# logger = get_logger(__name__)


class AddressRepository(AbstractRepository):

    def get_by_id(self, id: int) -> Address:
        addr = Address.query.get(id)
        if addr is None:
            raise NotFoundException("Address not found")
        return addr

    def create(self, addr: Address) -> Address:
        db.session.add(addr)
        db.session.commit()
        return addr

    def update(self, id: int, new_address: Address) -> Address:
        address = Address.query.get(id)
        if address is None:
            raise NotFoundException("Address not found")
        new_address_keys = [x for x in vars(new_address) if not x.startswith('_')]
        for key in new_address_keys:
            if new_address[key] != address[key]:
                setattr(address, key, new_address[key])
        db.session.commit()
        return address

    def delete(self, id: int) -> Address:
        address = Address.query.get(id)
        if address is None:
            raise NotFoundException("Address not found")
        db.session.delete(address)
        db.session.commit()
        return address
