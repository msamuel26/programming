def nilai_genap(value):
    output = True

    if value % 2 == 0:
        output = True
    else:
        output = False

    return output

nilai = int(input("Enter your number: "))

if nilai_genap(nilai):
    print("bilangan tersebut adalah bilangan genap")
else:
    print("bilangan tersebut adalah bilangan ganjil")