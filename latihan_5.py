# Define our 3 functions
def my_function():
    print("Hello From My Functions!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1, 2)
print(x)


def print_with_arg(param1, param2, param3):
    print("Hello %s, %s. Selamat datang %s"%(param1, param2, param3))

print_with_arg('Setip', 'lagi bobok', 'di jetracer bot kit')
