def testing(input):
    x = {}
    y = input.lower()
    for data in y:
        if data != " ":
            x[data] = y.count(data)
    return x

# print(testing("abaca dabra didi DADU"))

def testing_1(info):
    info_1 = info.lower()
    info_2 = info_1.split(" ")
    x = ""
    for i in info_2:
        for index, data in enumerate(i):
            if index % 2 == 0:
                x += data.upper()
            else:
                x += data
        x += " "
    return x

print(testing_1("abaca dabra didi"))

def testing_2(data):
    data_1 = data.lower()
    data_2 = data_1.split(" ")
    data_2.reverse()
    x = ""
    for data in data_2:
        for i in data:
            x += i
        x += " "
    return x 

# print(testing_2("abaca dabra didi DADU"))

def daftar_nilai(inputt):
    x = {}
    for data in inputt:
        if data[0] not in x:
            x[data[0]] = [0,0,0]
        if data[1] == "math":
            x[data[0]][0] = data[2]
        if data[1] == "english":
            x[data[0]][1] = data[2]
        if data[1] == "science":
            x[data[0]][2] = data[2]
    return x

print(daftar_nilai([["acong", "math", 10],
            ["badu", "english", 9],
            ["amoy", "science", 9],
            ["acong", "english", 8],
            ["badu", "science", 7],
            ["amoy", "english", 8],
            ["acong", "science", 8],
            ["badu", "math", 7],
            ["amoy", "math", 9]]
        ))