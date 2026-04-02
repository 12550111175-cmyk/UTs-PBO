class DiskonMixin:
    def hitung_diskon_persen(self, total, persen):
        return total - (total * persen / 100)

    def hitung_diskon_tetap(self, total, nominal):
        return max(0, total - nominal)