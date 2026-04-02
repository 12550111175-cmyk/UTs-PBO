from transaksi_penjualan import TransaksiPenjualan

class TokoSwalayan:
    def __init__(self):
        self.__daftar_barang = []
        self.__daftar_transaksi = []
    
    # Getter barang
    @property
    def daftar_barang(self):
        return self.__daftar_barang.copy()

    # Getter transaksi
    @property
    def daftar_transaksi(self):
        return self.__daftar_transaksi.copy()

    def tambah_barang(self, barang):
        self.__daftar_barang.append(barang)

    def cari_barang(self, nama):
        for b in self.__daftar_barang:
            if b.nama == nama:
                return b
        return None

    def buat_transaksi(self, pelanggan):
        transaksi = TransaksiPenjualan(pelanggan)
        self.__daftar_transaksi.append(transaksi)
        return transaksi