import time
from makanan import Makanan
from minuman import Minuman
from rumah_tangga import RumahTangga
from toko import TokoSwalayan
from laporan_stok import LaporanStok
from laporan_penjualan import LaporanPenjualan
from admin import Admin
from kasir import Kasir
from pelanggan import Pelanggan
from pembayaran_tunai import PembayaranTunai
from pembayaran_ewallet import PembayaranEWallet

# ================= WARNA =================
RESET = "\033[0m"
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"

# ================= UI =================
def garis():
    print(BIRU + "=" * 50 + RESET)

def header(judul):
    garis()
    print(BIRU + judul.center(50) + RESET)
    garis()

def sukses(teks):
    print(HIJAU + teks + RESET)

def error(teks):
    print(MERAH + teks + RESET)

def info(teks):
    print(KUNING + teks + RESET)

def loading(teks="Memproses"):
    print(teks, end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print()

def beep():
    print("\a", end="")

def format_rupiah(angka):
    return f"Rp{int(angka):,}".replace(",", ".")

def tampilkan_barang(daftar):
    garis()
    print(f"{'No':<3} {'Nama':<15} {'Harga':<12} {'Stok':<5} {'Keterangan'}")
    garis()

    for i, b in enumerate(daftar, start=1):
        print(f"{i:<3} {b.nama:<15} {format_rupiah(b.harga_jual):<12} {b.stok:<5} {b.info_barang()}")
    
    garis()

# ================= MAIN =================
def main():
    header("TOKO SWALAYAN RAYDY")

    admin = Admin("A01", "ayzahra")
    kasir = Kasir("K01", "radish")

    toko = TokoSwalayan()

    # DATA AWAL
    admin.tambah_barang(toko, Makanan("Roti", 10000, 8000, 20, "2026-12-01", diskon=10))
    admin.tambah_barang(toko, Minuman("Teh Botol", 5000, 3000, 30, "250ml", "2026-12-01", diskon=0))
    admin.tambah_barang(toko, RumahTangga("Sabun Cuci", 15000, 10000, 25, "Deterjen", diskon=5))

    while True:
        header("LOGIN")
        user_id = input("Masukkan ID (Admin/Kasir) atau 0 untuk keluar: ")

        if user_id == "0":
            sukses("Terima kasih 🙏")
            break

        # ================= ADMIN =================
        if user_id == admin.id_user:
            sukses(f"Login sebagai Admin: {admin.nama}")

            while True:
                header("MENU ADMIN")
                print("1. Lihat Barang")
                print("2. Tambah Barang")
                print("3. Hapus Barang")
                print("4. Lihat Laporan")
                print("0. Logout")

                pilih = int(input("Pilih: "))

                if pilih == 1:
                    tampilkan_barang(toko.daftar_barang)

                elif pilih == 2:
                    try:
                        nama = input("Nama: ")
                        harga = int(input("Harga jual: "))
                        modal = int(input("Harga modal: "))
                        stok = int(input("Stok: "))
                        diskon = int(input("Diskon (%): "))

                        barang_lama = None
                        for b in toko.daftar_barang:
                            if b.nama.lower() == nama.lower():
                                barang_lama = b
                                break

                        if barang_lama:
                            barang_lama.tambah_stok(stok)
                            sukses(f"Stok {barang_lama.nama} ditambah! Total: {barang_lama.stok}")
                            continue

                        print("Kategori:")
                        print("1. Makanan")
                        print("2. Minuman")
                        print("3. Rumah Tangga")

                        kategori = int(input("Pilih: "))

                        if kategori == 1:
                            exp = input("Expired: ")
                            barang = Makanan(nama, harga, modal, stok, exp, diskon=diskon)

                        elif kategori == 2:
                            ukuran = input("Ukuran: ")
                            exp = input("Expired: ")
                            barang = Minuman(nama, harga, modal, stok, ukuran, exp, diskon=diskon)

                        elif kategori == 3:
                            jenis = input("Jenis: ")
                            barang = RumahTangga(nama, harga, modal, stok, jenis, diskon=diskon)

                        else:
                            error("Kategori tidak valid!")
                            continue

                        admin.tambah_barang(toko, barang)
                        sukses("Barang berhasil ditambahkan!")

                    except Exception as e:
                        error(f"Error: {e}")

                elif pilih == 3:
                    try:
                        tampilkan_barang(toko.daftar_barang)
                        idx = int(input("Pilih nomor barang: "))
                        barang = toko.daftar_barang[idx - 1]
                        toko.daftar_barang.remove(barang)
                        sukses("Barang dihapus!")

                    except Exception as e:
                        error(f"Error: {e}")

                elif pilih == 4:
                    header("LAPORAN STOK")
                    laporan_stok = LaporanStok(toko.daftar_barang)
                    for nama, stok in laporan_stok.generate():
                        print(f"{nama}: {stok}")

                    header("LAPORAN PENJUALAN")
                    laporan_penjualan = LaporanPenjualan(toko.daftar_transaksi)
                    for i, total in enumerate(laporan_penjualan.generate(), start=1):
                        print(f"Transaksi {i}: {format_rupiah(total)}")

                elif pilih == 0:
                    break

        # ================= KASIR =================
        elif user_id == kasir.id_user:
            sukses(f"Login sebagai Kasir: {kasir.nama}")

            nama_pelanggan = input("Nama pelanggan: ")
            pelanggan = Pelanggan("P01", nama_pelanggan)

            transaksi = toko.buat_transaksi(pelanggan)

            while True:
                header("MENU KASIR")
                print("1. Lihat Barang")
                print("2. Cari Barang")
                print("0. Selesai")

                aksi = int(input("Pilih: "))

                if aksi == 0:
                    break

                if aksi == 1:
                    daftar = toko.daftar_barang

                elif aksi == 2:
                    keyword = input("Cari: ").lower()
                    daftar = [b for b in toko.daftar_barang if keyword in b.nama.lower()]

                    if not daftar:
                        error("Barang tidak ditemukan!")
                        continue
                else:
                    continue

                tampilkan_barang(daftar)

                try:
                    pilih_barang = int(input("Pilih barang: "))
                    barang = daftar[pilih_barang - 1]

                    jumlah = int(input("Jumlah: "))
                    transaksi.tambah_item(barang, jumlah)

                except Exception as e:
                    error(f"Error: {e}")

            try:
                loading("Menghitung total")
                total = transaksi.hitung_total()

                header("PEMBAYARAN")
                print("Total:", format_rupiah(total))

                print("1. Tunai")
                print("2. E-Wallet")
                metode = int(input("Pilih: "))

                if metode == 1:
                    uang = int(input("Uang: "))
                    loading("Memproses pembayaran")
                    pembayaran = PembayaranTunai(uang)
                    kembalian = pembayaran.bayar(total)
                    beep()

                    loading("Mencetak struk")
                    transaksi.tampilkan_struk("Tunai", uang, kembalian)

                elif metode == 2:
                    loading("Memproses pembayaran")
                    pembayaran = PembayaranEWallet()
                    pembayaran.bayar(total)
                    beep()

                    loading("Mencetak struk")
                    transaksi.tampilkan_struk("E-Wallet")

            except Exception as e:
                error(f"Error pembayaran: {e}")

        else:
            error("ID tidak dikenali!")


if __name__ == "__main__":
    main()