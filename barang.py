from abc import ABC, abstractmethod
from validation_mixin import ValidationMixin

class Barang(ABC, ValidationMixin):
    def __init__(self, nama, harga_jual, harga_modal, stok, kategori, diskon=0):

        self.validate_nama(nama)
        self.validate_harga(harga_jual)
        self.validate_stok(stok)

        self.nama = nama
        self.__harga_jual = harga_jual
        self.__harga_modal = harga_modal
        self.__stok = stok
        self.__diskon = diskon
        self.kategori = kategori

    @property
    def harga_jual(self):
        return self.__harga_jual

    @harga_jual.setter
    def harga_jual(self, value):
        if value <= 0:
            raise ValueError("Harga harus > 0")
        self.__harga_jual = value

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        if value < 0:
            raise ValueError("Stok tidak boleh negatif")
        self.__stok = value

    def tambah_stok(self, jumlah):
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            raise ValueError("Stok tidak cukup")
        self.__stok -= jumlah

    def get_harga_modal(self):
        return self.__harga_modal
    
    @property
    def diskon(self):
        return self.__diskon

    @diskon.setter
    def diskon(self, value):
        if value < 0 or value > 100:
            raise ValueError("Diskon harus 0-100")
        self.__diskon = value

    @abstractmethod
    def info_barang(self):
        pass
