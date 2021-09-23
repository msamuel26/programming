def nilai_ganjil(value):
    if value % 2 == 1:
        return True
    else:
        return False

if nilai_ganjil(101):
    print("nilai tersebut adalah ganjil")
else:
    print("nilai tersebut adalah genap")