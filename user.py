from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, id_user, nama):
        self.id_user = id_user
        self.nama = nama

    @abstractmethod
    def role(self):
        pass

    def info_user(self):
        return f"{self.nama} ({self.role()})"