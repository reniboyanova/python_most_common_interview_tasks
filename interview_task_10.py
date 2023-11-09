# 10. Write a Python Program to Check if a Number is a Strong Number?
# A Strong number is a special number whose sum of the all digit factorial should be equal to the number itself.
#
# For example - The given number is 145, we have to pick each digit and find the factorial 1! = 1, 4! = 24, and 5! = 120.
#
# Now, we will do the sum of the factorials, we get 1+24+120 = 145, which is exactly the same as the given number.
# So we can say that 145 is a strong number.

def factorial(n):
    if n <= 1:
        return n
    return factorial(n - 1) * n


def check_for_strong_number(num):
    if not isinstance(num, int):
        raise TypeError("Number must to be an integer!")

    if num < 0:
        raise ValueError("Number must to be a positive number!")

    numbers = []
    check_num = num

    while num > 0:
        num_to_append = num % 10
        num = num // 10
        numbers.append(factorial(num_to_append))

    return f"Number {check_num} {'is strong number' if sum(numbers) == check_num else 'is NOT strong number'}"


if __name__ == "__main__":
    print(check_for_strong_number(144))
    print(check_for_strong_number(145))