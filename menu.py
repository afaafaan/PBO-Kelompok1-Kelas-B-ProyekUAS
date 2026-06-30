from abstrak_interface import ProdukBakery
from rotiManis import RotiManis
from croissant import Croissant
from produk_kue_kering import ButterCookies, Muffin

# DATA PRODUK
daftar_produk = []

# FUNGSI MENU
def tambah_produk():
    print("\n" + "-"*40)
    print("JENIS PRODUK YANG AKAN DITAMBAH")
    print("1. Roti Manis")
    print("2. Croissant")
    print("3. Butter Cookies")
    print("4. Muffin")
    pilihan = input("Nomor yang dipilih: ")

    kode = input("Masukkan Kode Produk   : ")
    nama = input("Masukkan Nama Produk   : ")
    tahun = input("Masukkan Tahun Terbit  : ")
    biaya = int(input("Masukkan Biaya Produksi: "))
    harga = int(input("Masukkan Harga Jual    : "))
    n_pcs = int(input("Masukkan Jumlah Pcs    : "))

    if pilihan == "1":
        produk = RotiManis(kode, nama, {}, n_pcs, biaya, harga)
    elif pilihan == "2":
        produk = Croissant(kode, nama, {}, n_pcs, biaya, harga)
    elif pilihan == "3":
        produk = ButterCookies(kode, nama, {}, n_pcs, biaya, harga)
    elif pilihan == "4":
        produk = Muffin(kode, nama, {}, n_pcs, biaya, harga)
    else:
        print("Pilihan tidak valid!")
        return

    daftar_produk.append(produk)
    print("-"*40)
    print("Tambah Produk Sukses!")
    input("Tekan [ENTER] untuk kembali ke menu program")

def tampil_semua_produk():
    print("\n" + "-"*40)
    print("DATA SEMUA PRODUK")
    if len(daftar_produk) == 0:
        print("Belum ada produk yang ditambahkan.")
    else:
        for i, produk in enumerate(daftar_produk, 1):
            print(f"\nProduk {i}:")
            print(f"Nama Produk      : {produk.nama}")
            print(f"Kode Produk      : {produk.kode}")
            print(f"Biaya Produksi   : Rp{produk.biaya_produksi}")
            print(f"Harga Jual       : Rp{produk.harga_jual}")
    input("\nTekan [ENTER] untuk kembali ke menu program")

def kalkulator_profit():
    print("\n" + "-"*40)
    print("KALKULATOR PROFIT")
    print("Pilih jenis produk:")
    print("1. Roti Manis")
    print("2. Croissant")
    print("3. Butter Cookies")
    print("4. Muffin")
    pilihan = input("Nomor yang dipilih: ")

    produk_map = {
        "1": RotiManis("RM001", "Roti Manis", {}, 10, 15000, 25000),
        "2": Croissant("CR001", "Croissant", {}, 10, 20000, 35000),
        "3": ButterCookies("BC001", "Butter Cookies", {}, 10, 10000, 18000),
        "4": Muffin("MF001", "Muffin", {}, 10, 12000, 20000)
    }

    if pilihan not in produk_map:
        print("Pilihan tidak valid!")
        return

    produk = produk_map[pilihan]
    jumlah = int(input("Masukkan jumlah pcs yang akan diproduksi: "))
    profit = (produk.harga_jual - produk.biaya_produksi) * jumlah
    print("-"*40)
    print(f"Jenis Produk     : {produk.nama}")
    print(f"Jumlah Produksi  : {jumlah} pcs")
    print(f"Biaya Produksi   : Rp{produk.biaya_produksi * jumlah:,}")
    print(f"Total Pendapatan : Rp{produk.harga_jual * jumlah:,}")
    print(f"Estimasi Profit  : Rp{profit:,}")
    input("\nTekan [ENTER] untuk kembali ke menu program")

def simulasi_produksi():
    print("\n" + "-"*40)
    print("SIMULASI PROSES PRODUKSI")
    print("Pilih jenis produk:")
    print("1. Roti Manis")
    print("2. Croissant")
    print("3. Butter Cookies")
    print("4. Muffin")
    pilihan = input("Nomor yang dipilih: ")

    produk_map = {
        "1": RotiManis("RM001", "Roti Manis", {}, 10, 15000, 25000),
        "2": Croissant("CR001", "Croissant", {}, 10, 20000, 35000),
        "3": ButterCookies("BC001", "Butter Cookies", {}, 10, 10000, 18000),
        "4": Muffin("MF001", "Muffin", {}, 10, 12000, 20000)
    }

    if pilihan not in produk_map:
        print("Pilihan tidak valid!")
        return

    produk = produk_map[pilihan]
    print(f"\n=== Simulasi Produksi {produk.nama} ===")
    produk.pengadonan()
    if hasattr(produk, "pengembangan"):
        produk.pengembangan()
    produk.pemanggangan()
    if hasattr(produk, "topping"):
        produk.topping()
    produk.packaging()
    produk.labeling()
    input("\nTekan [ENTER] untuk kembali ke menu program")

# MENU UTAMA
def main():
    while True:
        print("\n" + "="*30)
        print("PROGRAM MENU HANARI BAKERY")
        print("-"*30)
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        print("="*30)
        pilihan = input("Nomor yang dipilih: ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            tampil_semua_produk()
        elif pilihan == "3":
            kalkulator_profit()
        elif pilihan == "4":
            simulasi_produksi()
        elif pilihan == "5":
            print("Terima kasih telah berbelanja di Hanari Bakery!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
