def sample_break(data):
    print('sample break')
    for value in data:
        if value == 5:
            break
        else:
            print(value)

def sample_continue(data):
    print('sample continue')
    for value in data:
        if value == 5:
            continue
        else:
            print(value)

o = [1,2,3,4,5,6,7,8,9,10]
sample_break(o)
print('')
sample_continue(o)