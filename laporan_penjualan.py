from laporan import Laporan

class LaporanPenjualan(Laporan):
    def __init__(self, daftar_transaksi):
        self.daftar_transaksi = daftar_transaksi

    def generate(self):
        return [t.total for t in self.daftar_transaksi]