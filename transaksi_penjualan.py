from diskon_mixin import DiskonMixin
from pelanggan import Pelanggan
from log_mixin import LogMixin
from validation_mixin import ValidationMixin
from detail_transaksi import DetailTransaksi
from datetime import datetime
from metode_pembayaran import MetodePembayaran

class TransaksiPenjualan(DiskonMixin, LogMixin, ValidationMixin, Pelanggan):
    def __init__(self, Pelanggan):
        self.id_transaksi = datetime.now().strftime("%Y%m%d%H%M%S")
        self.tanggal = datetime.now()
        self.daftar_item = []
        self.total = 0
        self.pelanggan = Pelanggan # 🔥 

    def tambah_item(self, barang, jumlah):
        barang.kurangi_stok(jumlah)
        item = DetailTransaksi(barang, jumlah)
        self.daftar_item.append(item)
        self.log(f"Tambah {barang.nama} sebanyak {jumlah}")

    def hitung_total(self):
        self.total = sum(item.subtotal for item in self.daftar_item)
        return self.total

    def total_setelah_diskon_persen(self, persen):
        total = self.hitung_total()
        return self.hitung_diskon_persen(total, persen)

    def total_setelah_diskon_tetap(self, nominal):
        total = self.hitung_total()
        return self.hitung_diskon_tetap(total, nominal)
    
    def proses_pembayaran(self, metode_pembayaran, total_bayar):
        return metode_pembayaran.bayar(total_bayar)
    
    def tampilkan_struk(self, metode, jumlah_bayar=None, kembalian=None):
        print("\n=== STRUK PEMBELIAN ===")
        self.hitung_total()
        
        if self.pelanggan:
            print(f"Pelanggan : {self.pelanggan.nama}")
            
        print("\nDaftar Belanja:")
        for item in self.daftar_item:
            b = item.barang
            print(f"- {b.nama} x{item.jumlah} "
                f"(Diskon {b.diskon}%) = Rp{int(item.subtotal)}")

        print(f"\nTotal: Rp{int(self.total)}")
        print(f"Metode Pembayaran: {metode}")

        if metode == "Tunai":
            print(f"Uang Dibayar: Rp{jumlah_bayar}")
            print(f"Kembalian: Rp{kembalian}")

        print("======================\n")