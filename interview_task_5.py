# 5. Write a program that check given an array of integers is monotonic or not.
# A = [6, 5, 4, 4]
# B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# C = [1, 1, 2, 3, 7]
# Output:
# True
# False
# True


def check_for_monotonic_arr(list_of_numbers):
    result_desc = True
    result_asc = True
    for index in range(1, len(list_of_numbers)):
        if list_of_numbers[index] > list_of_numbers[index - 1]:
            result_desc = False
        elif list_of_numbers[index] < list_of_numbers[index - 1]:
            result_asc = False

    return result_desc or result_asc

if __name__ == "__main__":
    print(check_for_monotonic_arr([6, 5, 4, 4]))
    print(check_for_monotonic_arr([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(check_for_monotonic_arr([1, 1, 2, 3, 7]))
    print(check_for_monotonic_arr([6, 5, 7, 4, 4]))