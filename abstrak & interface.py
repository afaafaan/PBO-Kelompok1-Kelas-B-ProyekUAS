from abc import ABC, abstractmethod

class IStandarisasi(ABC):
    @abstractmethod
    def packaging(self):
        pass

    @abstractmethod
    def labeling(self):
        pass

class ProdukBakery(IStandarisasi, ABC):
    def _init_(self, kode, nama, bahan_baku, n_pcs, biaya_produksi, harga_jual):
        self.kode = kode
        self.nama = nama
        self.bahan_baku = bahan_baku         
        self.n_pcs = n_pcs                    
        self.biaya_produksi = biaya_produksi  
        self.harga_jual = harga_jual          

    def info_dasar(self):
        print(f"\n[{self.kode}] {self.nama}")
        print(f"  - Standar Porsi Resep : {self.n_pcs} pcs")
        print(f"  - Biaya Produksi per resep : Rp {self.biaya_produksi:,.2f}")
        print(f"  - Harga Jual per resep     : Rp {self.harga_jual:,.2f}")
        print("  - Daftar Bahan Baku:")
        for bahan, jumlah in self.bahan_baku.items():
            print(f"    * {bahan}: {jumlah}")

    @abstractmethod
    def pengadonan(self):
        pass

    @abstractmethod
    def pemanggangan(self):
        pass