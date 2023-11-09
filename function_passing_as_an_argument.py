
# defining a decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()

# Defining lambda function
square = lambda x: x * x

# Defining lambda function
# and passing function as an argument
cube = lambda func: func ** 3

print("square of 2 is :" + str(square(2)))
print("\nThe cube of " + str(square(2)) + " is " + str(cube(square(2))))


my_list = [1, 2, 3, 4, 5]
a, b, *rest = my_list
print(rest)

my_list = [1, 2, 3, 4, 5]
first, *rest, last = my_list
print(f'first: {first}, rest: {rest}, last: {last}')
# Изход: first: 1, rest: [2, 3, 4], last: 5
my_dict = {"name": "Reni Boyanova", "age": 32, "profession": "Developer", "money": 20242024}
for key, value in my_dict.items():
    print(hash(key))