def sample_break(nilai):
    print('Sample break')
    for value in nilai:
        if value == 5:
            break
        else:
            print(value)

def sample_continue(nilai):
    print('Sample continue')
    for value in nilai:
        if value == 5:
            continue
        else:
            print(value)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sample_break(x)
print('')
sample_continue(x)