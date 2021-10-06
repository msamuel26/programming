def sample_break(value):
    print("Sample break")
    for gukguk in value:
        if gukguk == 3:
            break
        else:
            print(gukguk)

def sample_continue(value):
    print("Sample continue")
    for emprit in value:
        if emprit == 4:
            continue
        else:
            print(emprit)

a = [1, 2, 3, 4, 5, 6]
sample_break(a)
print('')
sample_continue(a)