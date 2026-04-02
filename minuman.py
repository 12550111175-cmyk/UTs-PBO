from barang import Barang
class Minuman(Barang):
    def __init__(self, nama, harga_jual, harga_modal, stok, ukuran, expired, diskon=0):
        super().__init__(nama, harga_jual, harga_modal, stok, diskon, "Minuman")
        self.ukuran = ukuran
        self.expired = expired  # TAMBAHAN

    def format_rupiah(angka):
        return f"Rp{int(angka):,}".replace(",", ".")
    def info_barang(self):
        return f"Kategori: {self.kategori} | Volume: {self.ukuran} | Exp: {self.expired}"