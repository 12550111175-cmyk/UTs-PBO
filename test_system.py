import unittest
from makanan import Makanan
from minuman import Minuman
from rumah_tangga import RumahTangga
from toko import TokoSwalayan
from pelanggan import Pelanggan
from pembayaran_tunai import PembayaranTunai


class TestSistemSwalayan(unittest.TestCase):

    def setUp(self):
        self.toko = TokoSwalayan()

        self.roti = Makanan("Roti", 10000, 8000, 10, "2026-12-01", diskon=10)
        self.teh = Minuman("Teh", 5000, 3000, 20, "250ml", "2026-12-01", diskon=0)

        # 🔥 pakai method resmi (enkapsulasi)
        self.toko.tambah_barang(self.roti)
        self.toko.tambah_barang(self.teh)

        self.pelanggan = Pelanggan("P01", "TestUser")

    # ================= ENKAPSULASI =================
    def test_enkapsulasi_barang(self):
        with self.assertRaises(AttributeError):
            _ = self.roti.__stok

        self.assertEqual(self.roti.stok, 10)

    # ================= TRANSAKSI =================
    def test_transaksi_mengurangi_stok(self):
        transaksi = self.toko.buat_transaksi(self.pelanggan)
        transaksi.tambah_item(self.roti, 2)

        self.assertEqual(self.roti.stok, 8)

    def test_total_dengan_diskon(self):
        transaksi = self.toko.buat_transaksi(self.pelanggan)
        transaksi.tambah_item(self.roti, 1)

        total = transaksi.hitung_total()

        # 10000 - 10% = 9000
        self.assertEqual(total, 9000)

    # ================= PEMBAYARAN =================
    def test_pembayaran_tunai(self):
        pembayaran = PembayaranTunai(20000)
        kembalian = pembayaran.bayar(15000)

        self.assertEqual(kembalian, 5000)

    def test_pembayaran_kurang(self):
        pembayaran = PembayaranTunai(10000)

        with self.assertRaises(ValueError):
            pembayaran.bayar(15000)

    # ================= VALIDASI =================
    def test_validasi_harga_negatif(self):
        with self.assertRaises(ValueError):
            Makanan("Salah", -1000, 500, 10, "2026", diskon=0)

    def test_validasi_stok_negatif(self):
        with self.assertRaises(ValueError):
            Minuman("Salah", 5000, 3000, -5, "250ml", "2026", diskon=0)

    def test_validasi_diskon(self):
        with self.assertRaises(ValueError):
            self.roti.diskon = 150

    # ================= LAPORAN STOK =================
    def test_laporan_stok(self):
        barang_list = self.toko.daftar_barang  # atau get_daftar_barang() kalau ada

        stok_list = [(b.nama, b.stok) for b in barang_list]

        self.assertIn(("Roti", 10), stok_list)
        self.assertIn(("Teh", 20), stok_list)

    # ================= LAPORAN PENJUALAN =================
    def test_laporan_penjualan(self):
        transaksi = self.toko.buat_transaksi(self.pelanggan)
        transaksi.tambah_item(self.roti, 1)

        transaksi_list = self.toko.daftar_transaksi  # atau getter

        laporan = [t.hitung_total() for t in transaksi_list]

        self.assertTrue(len(laporan) > 0)
        self.assertEqual(laporan[0], 9000)


if __name__ == "__main__":
    unittest.main(verbosity=2)