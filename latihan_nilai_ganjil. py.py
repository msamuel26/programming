def nilai_ganjil(nilai):
    check_result = False
    if nilai % 2 == 1:
        check_result = True
    else:
        check_result = False
    return check_result

# data = int(input("Select any number: "))
# if nilai_ganjil(data):
#     print(data, "adalah nilai ganjil")
# else:
#     print(data, "bukan nilai ganjil")

assert nilai_ganjil(3) == True
assert nilai_ganjil(4) == False