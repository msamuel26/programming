def nilai_ganjil(value):
    hasil_cek = None

    if value % 2 == 1:
        hasil_cek = True
    else:
        hasil_cek = False

    return hasil_cek

nilai = int(input('Nilai berapa yang akan dicek? : '))

if nilai_ganjil(nilai):
    print("nilai tersebut adalah ganjil")
else:
    print("nilai tersebut adalah genap")