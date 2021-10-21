# dari list numbers, agar cek nilai mana saja yang duplicate dan
# dia dupclicate berapa kali

# contoh
# [1,2,3,1,2,4,5,6,3,4]
# { 1:2, 2:2, 3:2, 4:2, 5:1, 6:1 }

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]


def create_summary(input_list):
    a = set(input_list)
    result = {}
    for value in a:
        hasil = input_list.count(value)
        # print(f"Value: {value}, Hasil: {hasil}")
        result[value] = hasil
    return result


setip = [1, 2, 1, 1]
# print(create_summary(setip))
mcpout = [2, 3, 4, 2, 3, 4, 5, 7]
# print(create_summary(mcpout))


def shown_dict_with_more_than_1_in_value(input_dict):
    output_dict = {}
    for key in input_dict:
        if input_dict[key] > 1:
            output_dict[key] = input_dict[key]
    return output_dict

# unyil = create_summary(numbers)
# print(unyil)
# print(shown_dict_with_more_than_1_in_value(unyil))


def even_number(input_int):
    output = False
    if input_int % 2 == 0:
        output = True
    return output


def odd_number(input_int):
    output = False
    if input_int % 2 == 1:
        output = True
    return output


def shown_only_even_key(input_dict):
    output_dict = {}
    for key in input_dict:
        if even_number(key):
            output_dict[key] = input_dict[key]
    return output_dict


def shown_only_odd_key(input_dict):
    output_dict = {}
    for key in input_dict:
        if odd_number(key):
            output_dict[key] = input_dict[key]
    return output_dict


def shown_only_even_key_and_with_more_than_1_in_value(input_dict):
    output_dict = {}
    for key in input_dict:
        if even_number(key) and input_dict[key] > 1:
            output_dict[key] = input_dict[key]
    return output_dict


def shown_only_odd_key_and_with_more_than_1_in_value(input_dict):
    output_dict = {}
    for key in input_dict:
        if odd_number(key) and input_dict[key] > 1:
            output_dict[key] = input_dict[key]
    return output_dict


def shown_only_even_key_and_with_more_than_1_in_value_with_param(input_dict, max_appeared):
    output_dict = {}
    max = 0
    for key in input_dict:
        if even_number(key) and input_dict[key] and max < max_appeared:
            output_dict[key] = input_dict[key]
            max = max + 1
    return output_dict

# Tolong tampil 3 key ganjil pertama dan 2 key genap pertama


def shown_first_3_odd_keys_and_first_3_even_keys(input_dict, input_odd, input_even):
    output_dict = {}
    max = 0
    for key in input_dict:
        if even_number(key) and max < input_even:
            output_dict[key] = input_dict[key]
            max = max + 1

    max = 0
    for key in input_dict:
        if odd_number(key) and max < input_odd:
            output_dict[key] = input_dict[key]
            max = max + 1
    return output_dict


def shown_first_11_odd_keys_and_first_14_even_keys(input_dict, input_count_odd, input_count_even):
    output_dict = {}
    max = 11
    for key in input_dict:
        if odd_number(key) and max > input_count_odd:
            output_dict[key] = input_dict[key]
            max = max - 1

    max = 14
    for key in input_dict:
        if even_number(key) and max > input_count_even:
            output_dict[key] = input_dict[key]
            max = max - 1
    return output_dict


def shown_odd_even_keys_sequentially(input_dict, input_count_odd, input_count_even):
    output_dict = {}

    tampung_ganjil = shown_only_odd_key(input_dict)
    tampung_genap = shown_only_even_key(input_dict)

    ganjil_reversed = dict(reversed(list(tampung_ganjil.items())))
    genap_reversed = dict(reversed(list(tampung_genap.items())))
    print(ganjil_reversed)
    print(genap_reversed)

    temp_count_odd = 0
    temp_count_even = 0

    while temp_count_odd < input_count_odd or temp_count_even < input_count_even:
        if temp_count_odd < input_count_odd:
            for nilai in ganjil_reversed:
                output_dict[nilai] = ganjil_reversed.pop(nilai)
                temp_count_odd = temp_count_odd + 1
                break
        
        if temp_count_even < input_count_even:
            for nilai in genap_reversed:
                output_dict[nilai] = genap_reversed.pop(nilai)
                temp_count_even = temp_count_even + 1
                break

    return output_dict 

unyil = create_summary(numbers)
# print(unyil)
# print("List yang menampilkan key yang hanya genap")
# print(shown_only_even_key(unyil))
# print('')
# print("List yang menampilkan key yang hanya ganjil")
# print(shown_only_odd_key(unyil))
# print('')
# print("List yang menampilkan key genap dan valuenya lebih dari 1")
# print(shown_only_even_key_and_with_more_than_1_in_value(unyil))
# print('')
# print("List yang menampilkan hanya key genap dan valuenya lebih dari 1 dengan menggunakan param")
# print(shown_only_even_key_and_with_more_than_1_in_value_with_param(unyil, 2))
# print('')
# print("List yang menampilkan 3 key ganjil pertama dan 3 key genap pertama")
# print(shown_first_3_odd_keys_and_first_3_even_keys(unyil, 3, 3))
# print('')
# print("List yang menampilkan 11 key ganjil pertama dan 14 key genap pertama")
# print(shown_first_11_odd_keys_and_first_14_even_keys(unyil, 0, 0))
print(shown_odd_even_keys_sequentially(unyil, 3, 2))


# print(shown_dict_with_more_than_1_in_value(unyil))

# print(create_summary(numbers))
# print(shown_dict_with_more_than_1_in_value(create_summary(numbers)))

# hasil = create_summary(numbers)
# print(hasil)
# print(type(hasil))
# print(shown_dict_with_more_than_1_in_value(hasil))



# test = [1,1,2,2,3,4,4,4,5]
# assert create_summary(test) == {1:2, 2:2, 3:1, 4:3, 5:1}
