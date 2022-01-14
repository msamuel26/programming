class Uang:
    def __init__(self, nominal, warna, bahan, bentuk):
            self.nominal = nominal
            self.warna = warna
            self.bahan = bahan
            self.bentuk =  bentuk

    def get_nominal(self):
            return self.nominal

    def get_warna(self):
            return self.warna

    def get_bentuk(self):
            return self.bentuk

    def get_bahan(self):
            return self.bahan

lima_ribu = Uang(5000, "coklat", "kertas", "kotak")
koin_seribu = Uang(1000, "silver", "nikel", "bulat")
koin_mangatus = Uang(500, "kuning keemasan", "nikel", "bulat") 

print(lima_ribu.get_bahan()) 
print(lima_ribu.get_nominal()) 
print(lima_ribu.get_bentuk())
print(lima_ribu.get_warna())            