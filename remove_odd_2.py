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

x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
assert remove_odd(x) == [2, 2, 4, 4]
print(x)

a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
assert remove_even(a) == [1, 1, 3, 3, 5, 5]
print(a)