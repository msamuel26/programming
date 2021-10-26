# Buat fungsi kali dengan 2 parameter, param2 dengan default nilai 2
# Nanti dia dipanggil dengan 1 atau 2 parameter

def kali(param1, param2 = 2):
    return param1 * param2 

def kali_dan_tambah(param1 = 2, param2 = 3, param3 = 4):
    return param1 * param2 + param3

print(kali(3, 5))
print(kali(4))
print(kali(param1=4))

print(kali_dan_tambah(1, 3, 5))
print(kali_dan_tambah(param1 = 1, param2 = 3, param3 = 5))
print(kali_dan_tambah(param3 = 5, param1 = 1, param2 = 3))
print(kali_dan_tambah())
print(kali_dan_tambah(param2 = 5))   