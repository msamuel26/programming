from distutils.errors import DistutilsClassError


some_dict = {1: 'eggs', 2: 'peanuts', 
             4: 'shellfish', 8: 'strawberries', 
             16: 'tomatoes', 32: 'chocolate', 
             64: 'pollen', 128: 'cats'}

def calculate(set_input, dict):
    output = 0
    for data in set_input:
        for key in dict:
            if data == key:
                output += dict[key]
    return output

def hitung(list_a, list_b, a_dict):
    reversed_dict = dict((value, key) for key, value in a_dict.items())

    a = set(list_a).intersection(set(list_b))
    b = set(list_a).difference(set(list_b))
    c = set(list_b).difference(set(list_a))

    numeric_intersec = calculate(a, reversed_dict)
    numeric_a_diff_b = calculate(b, reversed_dict)
    numeric_b_diff_a = calculate(c, reversed_dict)

    jumlah_a = numeric_intersec + numeric_a_diff_b
    jumlah_b = numeric_intersec + numeric_b_diff_a

    sisa = sum(a_dict) - numeric_intersec - numeric_a_diff_b - numeric_b_diff_a
    return [jumlah_a, jumlah_b, numeric_intersec,sisa] 

print(hitung(["eggs", "peanuts"], ["shellfish", "strawberries"], some_dict))