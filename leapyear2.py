def check_leap_year(year):
    leap = False
    if year > 1582:
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
    return leap

# data = int(input("Select any number: "))
# if check_leap_year(data):
#     print(data, "is leap year")
# else:
#     print(data, "is not leap year")

assert check_leap_year(1584) == True
assert check_leap_year(1991) == False
assert check_leap_year(1992) == True
assert check_leap_year(2000) == True
assert check_leap_year(2020) == True
assert check_leap_year(2024) == True
assert check_leap_year(2028) == True
assert check_leap_year(2032) == True
assert check_leap_year(2100) == False
assert check_leap_year(2200) == False
assert check_leap_year(2400) == True