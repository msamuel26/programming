def ingin_mengecek_bilangan_prima(value):
    marker = True
    if value > 1:
        for m in range(2, value):
            if value % m == 0:
                marker = False
                break
    return marker
    
test = int(input("Please choose your number: "))
if ingin_mengecek_bilangan_prima(test):
    print(test, "adalah bilangan prima")
else:
    print(test, "bukan bilangan prima")