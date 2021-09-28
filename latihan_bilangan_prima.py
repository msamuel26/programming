def check_prime_number(value):
    marker = True
    if value > 1:
        for x in range(2, value):
            if value % x == 0:
                marker = False
                break
    return marker

assert check_prime_number(3) == True
assert check_prime_number(4) == False
assert check_prime_number(7) == True
assert check_prime_number(9) == False
assert check_prime_number(17) == True