# 3. Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

# Input : [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Output : {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}


# 1st variant:

def count_occurrence(input_list):
    dict_to_return = {}
    for num in input_list:
        count = input_list.count(num)
        dict_to_return[num] = count

    return dict_to_return

# 2nd variant

from collections import defaultdict


def count_occurrence_2(input_list):
    count_dict = defaultdict(int)
    for num in input_list:
        count_dict[num] += 1

    return dict(count_dict)


if __name__ == "__main__":
    print(count_occurrence([11, 45, 8, 11, 23, 45, 23, 45, 89]))