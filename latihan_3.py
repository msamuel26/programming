numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

def create_summary(list):
    a = set(list)
    res = {}
    for key in a:
        hasil = list.count(key)
        res[key] = hasil
    return res

# prin t(create_summary(numbers))

list = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]
assert create_summary(list) == {1:2, 2:2, 3:4, 4:2, 5:2}

def shown_dict_with_more_than_1_in_value(dict):
    res = {}
    for key in dict:
        if dict[key] > 1:
            res[key] = dict[key]
    return res

unyil = create_summary(numbers)
print(unyil)
print(shown_dict_with_more_than_1_in_value(unyil))

print(shown_dict_with_more_than_1_in_value(create_summary(numbers))) 