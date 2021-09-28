# The Gregorian leap year rule is:
#   1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#   2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#   3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#   4. The year is a leap year (it has 366 days).
#   5. The year is not a leap year (it has 365 days).
#   from https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
# 
#   Check your function with this leap calculator
#   https://www.omnicalculator.com/everyday-life/leap-year#what-is-a-leap-year

def check_leap_year(year):
    leap = False
    # https://www.history.com/news/6-things-you-may-not-know-about-the-gregorian-calendar
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