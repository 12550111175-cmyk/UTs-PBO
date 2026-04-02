from barang import Barang

class RumahTangga(Barang):
    def __init__(self, nama, harga_jual, harga_modal, stok, jenis, diskon=0):
        super().__init__(nama, harga_jual, harga_modal, stok, "Rumah Tangga", diskon)
        self.jenis = jenis  # contoh: sabun, deterjen, dll

    def format_rupiah(angka):
        return f"Rp{int(angka):,}".replace(",", ".")
    def info_barang(self):
        return f"Kategori: {self.kategori} - {self.jenis}"