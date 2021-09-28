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

test = int(input("Select any number: "))
if check_leap_year(test):
    print(test, "is leap year")
else:
    print(test, "is not leap year") 