def check_prime_number(value):
    flag = False
    if value > 1:
        for i in range(2, value):
            if value % 1 == 0:
                flag = True
                break
    return not flag

test = int(input("Please select any number: "))
if check_prime_number(test):
    print(test, "is prime number")
else:
    print(test, "isn't prime number") 