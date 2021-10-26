def kali_kali_bagi(param1 = 5, param2 = 4, param3 = 3, param4 = 2):
    return param1 * param2 * param3 / param4

assert kali_kali_bagi(5, 4, 3, 2) == 30
assert kali_kali_bagi(1, 2, 3, 4) == 1.5
assert kali_kali_bagi() == 30
assert kali_kali_bagi(param3 = 5, param2 = 4) == 50
assert kali_kali_bagi(param3 = 6) == 60