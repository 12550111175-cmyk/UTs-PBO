from user import User
from validation_mixin import ValidationMixin
from transaksi_penjualan import TransaksiPenjualan

class Kasir(User, ValidationMixin):

    def role(self):
        return "Kasir"

    def buat_transaksi(self):
        self.validate_access(self, "Kasir")
        return TransaksiPenjualan()