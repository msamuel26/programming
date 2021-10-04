def remove_all(list, value):
    print("Jumlah", value, "di list", list, "adalah", list.count(value))
    jumlah = list.count(value)
    while jumlah > 0:
        print("List sebelum remove", list)
        list.remove(value)
        print("List setelah remove", list)
        jumlah = list.count(value)
    return list

i = [3, 3, 1, 2, 7, 6, 8, 8, 8, 2, 4, 5, 5, 5, 8]
remove_all(i, 8)