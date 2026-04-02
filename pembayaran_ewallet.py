from metode_pembayaran import MetodePembayaran

class PembayaranEWallet(MetodePembayaran):
    def __init__(self, saldo):
        self.saldo = saldo

    def bayar(self, total):
        if self.saldo < total:
            raise ValueError("Saldo tidak cukup")
        self.saldo -= total
        return self.saldo