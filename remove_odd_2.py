def is_odd(value):
    output = False
    if value % 2 == 1:
        output = True
    return output

def remove_odd(list):
    list.sort()
    dumy = list.copy()
    for value in dumy:
        if is_odd(value):
            list.remove(value)
    return list

p = [1, 2, 7, 8, 4, 3, 6, 8, 4, 6, 7, 5]
assert remove_odd(p) == [2, 4, 4, 6, 6, 8, 8]
print(p)
