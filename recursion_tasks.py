# 2.Write a program to find nth fibonacci number with recursion?
# A Fibonacci series is a series in which next number is a sum of previous two numbers.
#
# For example : 0, 1, 1, 2, 3, 5, 8
# First Fibonacci number is 0, second is 1, third is 2 and etc.
# Input: fib(2)
# Output: 1
# After implemetation of this task: Write a Python program to check if a given number is a Fibonacci number or not.
# Input: 8
# Output: True


def fibonacci(n):
    print(n)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * (power(base, exp - 1))

# Кулите на Ханой!
def toh(n, start, end, aux):
    if (n == 1):
        print("Move disk 1 from", start, "to", end)
        return
    toh(n - 1, start, aux, end)
    print("Move disk", n, "from", start, "to", end)
    toh(n - 1, aux, end, start)


if __name__ == "__main__":
    # n = 5
    # result = fibonacci(n)
    # print(result)
    #
    # print(list_sum([2, 4, 5, 6, 7]))
    #
    # print(factorial(5))
    toh(5, "I", "II", "III")
