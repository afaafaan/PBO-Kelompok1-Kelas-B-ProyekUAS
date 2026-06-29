from abstrak_interface import ProdukBakery
class ButterCookies(ProdukBakery):
    def pengadonan(self):
        print(f"-> [Proses Pengadonan {self.nama}]: Mengocok mentega berkualitas tinggi dan gula halus hingga mengembang (creaming method), lalu melipat tepung terigu secara perlahan.")

    def pemanggangan(self):
        print(f"-> [Proses Pemanggangan {self.nama}]: Dipanggang dengan suhu rendah 150°C selama 25 menit agar kering merata tanpa gosong.")

    def topping(self):
        print(f"-> [Proses Topping {self.nama}]: Diberi taburan gula kristal halus atau hiasan choco chip di atasnya sebelum/setelah dipanggang.")

    def packaging(self):
        print(f"-> [Packaging {self.nama}]: Disusun rapi di dalam toples mika plastik tebal transparan ukuran 500g dengan lapisan seal.")

    def labeling(self):
        print(f"-> [Labeling {self.nama}]: Ditempel segel stiker melingkar pada toples dengan logo Hanari Bakery.")

class Muffin(ProdukBakery):
    def pengadonan(self):
        print(f"-> [Proses Pengadonan {self.nama}]: Menggunakan muffin method (mencampur bahan kering dan bahan basah secara terpisah, lalu disatukan cepat tanpa overmix).")

    def pengembangan(self):
        print(f"-> [Proses Pengembangan {self.nama}]: Adonan diistirahatkan sejenak di dalam cup kertas agar struktur gluten rileks sebelum dipanggang.")

    def pemanggangan(self):
        print(f"-> [Proses Pemanggangan {self.nama}]: Dipanggang dengan suhu 190°C selama 20 menit hingga bagian atasnya merekah (dome terbentuk).")

    def topping(self):
        print(f"-> [Proses Topping {self.nama}]: Diberi taburan keju parut atau potongan buah kering di atas adonan cup.")

    def packaging(self):
        print(f"-> [Packaging {self.nama}]: Dimasukkan ke dalam boks karton sekat isi 4 atau isi 6.")

    def labeling(self):
        print(f"-> [Labeling {self.nama}]: Sablon logo Hanari Bakery pada penutup boks karton.")
