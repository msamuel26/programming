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

# print(testing_1("abaca dabra didi"))

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
    i = {}
    for data in inputt:
        if data[0] not in i:
            i[data[0]] = [0,0,0]
        if data[1] == "math":
            i[data[0]][0] = data[2]
        elif data[1] == "english":
            i[data[0]][1] = data[2]
        elif data[1] == "science":
            i[data[0]][2] = data[2]
    return i

# print(daftar_nilai([["acong", "math", 10],
#             ["badu", "english", 9],
#             ["amoy", "science", 9],
#             ["acong", "english", 8],
#             ["badu", "science", 7],
#             ["amoy", "english", 8],
#             ["acong", "science", 8],
#             ["badu", "math", 7],
#             ["amoy", "math", 9]]
#         ))

class ShowRanking:
    def __init__(self):
        self.input = None 
        self.i = {}

    def ranking(self, input):
        for data in input:
            if data[0] not in self.i:
                self.i[data[0]] = [0,0,0,0]
            if data[1] == "math":
                self.i[data[0]][0] = data[2]
            elif data[1] == "english":
                self.i[data[0]][1] = data[2]
            elif data[1] == "science":
                self.i[data[0]][2] = data[2]
            # self.i[data[0]][-1] += data[2]
        y = self.i.items()
        for item in y:
            c = item[1][0] + item[1][1] + item[1][2]
            item[1][-1] += c
        results = sorted([[name, score1, score2, score3, total]
            for name, (score1, score2, score3, total) in self.i.items()],
            key=lambda n: (n[4], n[3]), reverse=True)
        return results  

a = ShowRanking()
print(a.ranking([["acong", "math", 10],
 ["badu", "english", 9],
 ["amoy", "science", 9],
 ["acong", "english", 8],
 ["badu", "science", 7],
 ["amoy", "english", 8],
 ["acong", "science", 8],
 ["badu", "math", 7],
 ["amoy", "math", 9]]
))

class Saring:
    def __init__(self):
        self.data = []

    def saring(self, input, name):
        for data in input:
            if data[0] == name:
                self.data.append(data)
        return self.data

i = Saring()
print(i.saring([["acong", "math", 10],
 ["badu", "english", 9],
 ["amoy", "science", 9],
 ["acong", "english", 8],
 ["badu", "science", 7],
 ["amoy", "english", 8],
 ["acong", "science", 8],
 ["badu", "math", 7],
 ["amoy", "math", 9]], "acong"
))

class Saring2:
    def __init__(self, input):
        self.data = []
        self.input = input 

    def saring(self, name):
        self.data = []
        for data in self.input:
            if data[0] == name:
                self.data.append(data)
        return self.data 

e = Saring2([["acong", "math", 10],
 ["badu", "english", 9],
 ["amoy", "science", 9],
 ["acong", "english", 8],
 ["badu", "science", 7],
 ["amoy", "english", 8],
 ["acong", "science", 8],
 ["badu", "math", 7],
 ["amoy", "math", 9]])
print(e.saring("acong"))
print(e.saring("badu")) 