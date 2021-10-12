from __future__ import annotations
from abc import ABC, abstractmethod
from connection import *

class State(ABC):
    @property
    def connection(self) -> Connection:
        return self._connection

    @connection.setter
    def connection(self, connection: Connection) -> None:
        self._connection = connection

    @abstractmethod
    def run(self) -> None:
        pass
