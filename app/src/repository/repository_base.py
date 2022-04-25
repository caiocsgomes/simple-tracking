from abc import ABC, abstractmethod

from src.utils.database import db


class AbstractRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> db.Model:
        pass

    @abstractmethod
    def create(self, obj: db.Model) -> db.Model:
        pass

    @abstractmethod
    def update(self, id: int, obj: db.Model) -> db.Model:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
