from user import User
from validation_mixin import ValidationMixin

class Admin(User, ValidationMixin):

    def role(self):
        return "Admin"

    def tambah_barang(self, toko, barang):
        self.validate_access("Admin")
        toko.tambah_barang(barang)
