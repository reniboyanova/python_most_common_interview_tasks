# 7. Write a python program to find h.c.f. of two numbers
#
# For any two numbers that are inputs given by the user, we have to calculate and print the h.c.f. of that numbers.
# Case1: If the user inputs the numbers 4 and 6.
#
#
#             then the output should be '2'.
#
# Case2: If the user inputs the numbers 5 and 7.
#
#             then the output should be '1'.

def find_h_c_f(num1, num2):
    range_number = min(num1, num2)
    highest_num_to_divide = 0

    for num in range(1, range_number + 1):
        if (num1 % num == 0) and (num2 % num == 0):
            if highest_num_to_divide < num:
                highest_num_to_divide = num

    print(highest_num_to_divide)

# алгоритъма на Евклид.
def find_h_c_f_2(num1, num2):
    print(f"Initial values: num1 = {num1}, num2 = {num2}")

    while num2:
        print(f"Current values: num1 = {num1}, num2 = {num2}")

        num1, num2 = num2, num1 % num2

    print(f"HCF: {num1}")


if __name__ == "__main__":
    find_h_c_f(16, 24)
    find_h_c_f_2(16, 24)
