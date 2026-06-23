from abc import ABC, abstractmethod

class Baking(ABC):
    @abstractmethod
    def baking(self):
        pass

class Packaging(ABC):
    @abstractmethod
    def packaging(self):
        pass

class Labeling(ABC):
    @abstractmethod
    def labeling(self):
        pass

class ProdukBakery(ABC, Baking, Packaging, Labeling):
    def __init__(self, nama_produk, kode_produk, biaya_produksi, harga_jual, bahan_baku):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.biaya_produksi = biaya_produksi  
        self.harga_jual = harga_jual          
        self.bahan_baku = bahan_baku          

    @abstractmethod
    def pengadonan(self):
        pass
    def pengembangan(self):
        pass
    def topping(self):
        pass
    def hitung_estimasi_profit(self, jumlah_pcs, n_pcs_resep=1):
        biaya_per_pcs = self.biaya_produksi / n_pcs_resep
        harga_per_pcs = self.harga_jual / n_pcs_resep
        profit_per_pcs = harga_per_pcs - biaya_per_pcs
        return profit_per_pcs * jumlah_pcs