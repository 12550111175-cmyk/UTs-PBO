from metode_pembayaran import MetodePembayaran

class PembayaranTunai(MetodePembayaran):
    def __init__(self, uang_dibayar):
        self.uang_dibayar = uang_dibayar

    def bayar(self, total):
        if self.uang_dibayar < total:
            raise ValueError("Uang tidak cukup")
        kembalian = self.uang_dibayar - total
        return kembalian