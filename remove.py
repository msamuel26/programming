def remove_all(data, value):
    total_data = data.count(value)
    print("jumlah ", value, " adalah ", total_data)
    while total_data > 0:
        data.remove(value)
        print("isi list saat ini adalah ", data)
        total_data = total_data - 1
        print('total data saat ini adalah', total_data)
    return data

# a = [4, 4, 5, 6, 7, 9, 4, 4]

# remove_all(a, 4)

x = [2, 4, 3, 5, 7, 2, 2, 3]
remove_all(x, 2)

remove_all([2, 4, 3, 5, 7, 2, 2, 3], 2)