class ValidationMixin:

    def validate_harga(self, harga):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")

    def validate_stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")

    def validate_nama(self, nama):
        if not nama or not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        
    def validate_access(self, user, required_role):
        if user.role() != required_role:
            raise PermissionError(
                f"Akses ditolak! Dibutuhkan role: {required_role}"
            )
    def validate_access(self, role):
        if self.role() != role:
            raise Exception("Akses ditolak!")