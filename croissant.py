class Croissant(ProdukBakery):
    def pengadonan(self):
        print(f"-> [Proses Pengadonan {self.nama}]: Membuat adonan dasar (détrempe), diistirahatkan, lalu dilipat berulang kali dengan teknik laminasi korsvet (butter sheet).")

    def pengembangan(self):
        print(f"-> [Proses Pengembangan/Proofing {self.nama}]: Di-proofing dengan suhu stabil (maks 26°C agar butter tidak meleleh) selama 2 jam.")

    def pemanggangan(self):
        print(f"-> [Proses Pemanggangan {self.nama}]: Dipanggang dengan suhu tinggi 200°C di awal, lalu diturunkan ke 180°C hingga terbentuk lapisan pastry yang renyah.")

    def packaging(self):
        print(f"-> [Packaging {self.nama}]: Dimasukkan ke dalam kotak kraft paper box eksklusif.")

    def labeling(self):
        print(f"-> [Labeling {self.nama}]: Diberi hang-tag premium 'Hanari Boulangerie' beserta instruksi penghangatan ulang.")
