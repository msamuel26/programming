def is_odd(value):
    output = False
    if value % 2 == 1:
        output = True
    return output

def remove_odd(list):
    list.sort()
    for value in list:
        if is_odd(value):
            list.remove(value)
    return list

o = [1, 2, 3, 4, 5, 6, 6]
assert remove_odd(o) == [2, 4, 6, 6]
print(o)
b = [1, 2, 4, 3, 7, 8]
assert remove_odd(b) == [2, 4, 8]
remove_odd(b)
print(b)