from diskon_mixin import DiskonMixin

class DetailTransaksi(DiskonMixin):

    def __init__(self, barang, jumlah):
        self.barang = barang
        self.jumlah = jumlah
        self.subtotal = self.hitung_subtotal()

    def hitung_subtotal(self):
        harga = self.barang.harga_jual
        diskon = self.barang.diskon

        harga_setelah_diskon = self.hitung_diskon_persen(harga, diskon)
        return harga_setelah_diskon * self.jumlah