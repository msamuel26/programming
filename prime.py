def check_prime_number(value):
    flag = False
    if value > 1:
        for i in range(2, value):
            if value % i == 0:
                flag = True
                break
    return not flag

test = int(input('Enter your number: '))
if check_prime_number(test):
    print(test, "is prime number")
else:
    print(test, "is not prime number")