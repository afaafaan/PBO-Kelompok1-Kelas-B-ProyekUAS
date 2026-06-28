# CONTOH - Tampilan Menu

class rotimanis:
    nama = "Roti Manis"
    kode = "RM001"
    biaya_produksi = 15000
    harga_jual = 25000
    def pengadonan(self): print("Mengadon adonan roti manis...")
    def pengembangan(self): print("Mengembangkan adonan selama 1 jam...")
    def pemanggangan(self): print("Memanggang roti manis pada suhu 180°C selama 20 menit...")

class croissant:
    nama = "Croissant"
    kode = "CR001"
    biaya_produksi = 20000
    harga_jual = 35000
    def pengadonan(self): print("Mengadon adonan croissant dengan butter...")
    def pengembangan(self): print("Mengembangkan adonan croissant selama 2 jam...")
    def pemanggangan(self): print("Memanggang croissant pada suhu 200°C selama 25 menit...")

class buttercookies:
    nama = "Butter Cookies"
    kode = "BC001"
    biaya_produksi = 10000
    harga_jual = 18000
    def pengadonan(self): print("Mengadon adonan butter cookies...")
    def pemanggangan(self): print("Memanggang butter cookies pada suhu 160°C selama 15 menit...")
    def topping(self): print("Menambahkan topping choco chips...")

class muffin:
    nama = "Muffin"
    kode = "MF001"
    biaya_produksi = 12000
    harga_jual = 20000
    def pengadonan(self): print("Mengadon adonan muffin...")
    def pengembangan(self): print("Mengembangkan adonan muffin selama 30 menit...")
    def pemanggangan(self): print("Memanggang muffin pada suhu 175°C selama 20 menit...")
    def topping(self): print("Menambahkan topping blueberry...")

# =============================================
# DATA PRODUK
# =============================================
daftar_produk = []

# =============================================
# FUNGSI MENU
# =============================================

def tambah_produk():
    print("\n" + "-"*40)
    print("JENIS PRODUK YANG AKAN DITAMBAH")
    print("1. Roti Manis")
    print("2. Croissant")
    print("3. Butter Cookies")
    print("4. Muffin")
    pilihan = input("Nomor yang dipilih: ")

    if pilihan == "1":
        produk = rotimanis()
    elif pilihan == "2":
        produk = croissant()
    elif pilihan == "3":
        produk = buttercookies()
    elif pilihan == "4":
        produk = muffin()
    else:
        print("Pilihan tidak valid!")
        return

    produk.nama = input("Masukkan Nama Produk   : ")
    produk.kode = input("Masukkan Kode Produk   : ")
    produk.biaya_produksi = int(input("Masukkan Biaya Produksi: "))
    produk.harga_jual = int(input("Masukkan Harga Jual    : "))
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

    produk_map = {"1": rotimanis(), "2": croissant(), "3": buttercookies(), "4": muffin()}
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

    produk_map = {"1": rotimanis(), "2": croissant(), "3": buttercookies(), "4": muffin()}
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
    input("\nTekan [ENTER] untuk kembali ke menu program")

# =============================================
# MENU UTAMA
# =============================================

def main():
    while True:
        print("\n" + "="*20)
        print("MENU PROGRAM HANARI BAKERY")
        print("-"*30)
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        print("="*20)
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
            print("Terima kasih telah menggunakan Hanari Bakery System!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()