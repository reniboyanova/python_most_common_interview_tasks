"""
Input : test_list = [[(4, 5), (3, 2)], [(2, 2)]]
Output : {4: 1, 5: 1, 3: 1, 2: 3}

Input : test_list = [[(4, 5), (3, 2)]]
Output : {4: 1, 5: 1, 3: 1, 2: 1}
"""

from collections import Counter

def frequency_count(elements):
    flat_list = [element for sublist in elements for tuple_element in sublist for element in tuple_element]
    print(flat_list)
    count_dict = dict(Counter(flat_list))
    return count_dict


if __name__ == "__main__":
    print(frequency_count([[(4, 5), (3, 2)], [(2, 2)]]))