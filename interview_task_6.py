# 6. Write a program to check a number is Armstrong or not in python programming language
# What is Armstrong Number?
# It is a number that is equal to the sum of cube of its digits.
# For eg: 153, 370 etc.
# Let's see it practically by calculating it,
#
# Suppose I am taking 153 for an example
#
# First calculate the cube of its each digit
#
#   1^3 = (1*1*1) = 1
#
#   5^3 = (5*5*5) = 125
#
#   3^3= (3*3*3) = 27
#
# Now adds the cube
#
#   1+125+27 = 153
#
# It means 153 is an Armstrong number.


def check_if_number_is_armstrong(num):
    num_to_check = num
    digits = []
    while num > 0:
        digit_to_add = num % 10
        digits.append(digit_to_add)
        num = num // 10

    sum_of_digits = sum(digit ** 3 for digit in digits)

    if sum_of_digits == num_to_check:
        return f"{num_to_check} is ARMSTRONG!"
    return f"{num_to_check} is NOT ARMSTRONG!"


# second variant:
def check_if_number_is_armstrong_2(num):
    num_str = str(num)
    num_digits = [int(digit) for digit in num_str]
    sum_of_digits = sum(digit ** 3 for digit in num_digits)

    return f"{num} is {'ARMSTRONG' if sum_of_digits == num else 'NOT ARMSTRONG'}"




if __name__ == "__main__":
    print(check_if_number_is_armstrong(477))
