# 1. Write a function that prints all duplicate items from a given list

# Input: [10, 20, 30, 30, 60, 40, 30, 60, 70, 80]
# Expected Output: -
#
# [30, 60]

def print_duplicate_reni(list_of_nums):
    """
    A function that return list with only duplicates values from a first given list
    :param list_of_nums:
    :return: list
    """
    list_to_return = []
    for num in list_of_nums:

        counting = list_of_nums.count(num)
        if counting > 1:
            list_to_return.append(num)

    return list(set(list_to_return))


def print_duplicate_2(list_of_nums):
    seen = set()
    duplicates = set()
    for num in list_of_nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)


if __name__ == "__main__":
    print(print_duplicate_reni([10, 20, 30, 30, 60, 40, 30, 60, 70, 80]))
    print(print_duplicate_2([10, 20, 30, 30, 60, 40, 30, 60, 70, 80]))

