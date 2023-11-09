# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)

# Пример 1: Декоратор, който измерва времето за изпълнение на функция

import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} изпълнена за {end_time - start_time} секунди")
        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)


slow_function()


# Пример 2: Декоратор, който валидира входни данни

def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Всички аргументи трябва да са цели числа")
        return func(*args, **kwargs)

    return wrapper


@validate_input
def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)


# result = add_numbers("3", 5)  # Този ред ще предизвика ValueError

# Пример 3: Декоратор, който умножава резултата по 2

def multiply_by_two_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@multiply_by_two_decorator
def square(x):
    return x * x


result = square(4)  # Резултатът ще бъде 32 (4 * 4 * 2)

print(result)
