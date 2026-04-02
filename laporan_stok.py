from laporan import Laporan

class LaporanStok(Laporan):
    def __init__(self, daftar_barang):
        self.daftar_barang = daftar_barang

    def generate(self):
        return [(b.nama, b.stok) for b in self.daftar_barang]