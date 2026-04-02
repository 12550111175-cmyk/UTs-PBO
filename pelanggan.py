from user import User

class Pelanggan(User):
    def __init__(self, id_pelanggan, nama):
        self.id_pelanggan = id_pelanggan
        self.nama = nama

    def role(self):
        return "Pelanggan"

    def info(self):
        return f"{self.nama} - {self.nama}"