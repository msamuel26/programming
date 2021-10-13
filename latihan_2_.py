# Tolong cetak 7 bilangan pertama atas list

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

TOTAL_PRINT = 7

def print_first_17_numbers(list, value):
    index = 0
    while value > 0:
        print("Nilai list di index: ", index, "adalah", list[index])
        index = index + 1
        value = value - 1

# print_first_17_numbers(numbers, TOTAL_PRINT)

def print_first_number_from(list, nilai, value):
    index = list.index(value)
    while nilai > 0:
        print("Nilai list index ke ", index, "adalah", list[index])
        index = index + 1
        nilai = nilai - 1

print_first_number_from(numbers, TOTAL_PRINT, 950)



def print_last_number(list, value):
    index = len(list) - value
    while value > 0:
        print("Nilai list index ke ", index, " adalah ", list[index])
        index = index + 1
        value = value - 1

# print_last_number(numbers, 5)

# print(len(numbers))

# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]

