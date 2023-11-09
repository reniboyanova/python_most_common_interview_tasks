# 8 . Write a Python program to find l.c.m. of two numbers
# For any two numbers given by the user as an input, we have to calculate and print the l.c.m. of that numbers using python programming language.
# Case1: If the user inputs the numbers 4 and 6.
#
#              then the output should be '12'.
#
# Case2: If the user inputs the numbers 5 and 7.
#
#             then the output should be '35'.


def find_l_c_m(num1, num2):
    highest_result = num1 * num2
    lowest_result = max(num1, num2)
    result = highest_result

    for num in range(highest_result, lowest_result - 1, - 1):
        if (num % num1 == 0) and (num % num2 == 0) and num < result:
            result = num

    print(f"Result is: {result}")


# Second variant:
def find_l_c_m_2(num1, num2):
    # Намиране на по-голямото число между num1 и num2
    max_num = max(num1, num2)

    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break
        max_num += 1

    print(f"LCM: {lcm}")


if __name__ == "__main__":
    find_l_c_m(4, 6)
    find_l_c_m_2(4, 6)
