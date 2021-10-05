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

def remove_even(list):
    list.sort()
    dumy = list.copy()
    for value in dumy:
        if not is_odd(value):
            list.remove(value)
    return list

l = [1, 2, 3, 6, 7, 2, 4, 6, 1, 2, 8, 6, 4]
assert remove_odd(l) == [2, 2, 2, 4, 4, 6, 6, 6, 8]
print(l)

i = [1, 2, 3, 6, 7, 2, 4, 6, 1, 2, 8, 6, 4]
assert remove_even(i) == [1, 1, 3, 7]
print(i)