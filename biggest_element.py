"""
Намиране на най-голям елемент в списък: Напишете функция, която приема списък и намира най-големия елемент в него.
"""

sqn_numbers = [1, 3, 5, 12, 34, 89, 0, -3, 109, 2, 3, 56]

if __name__ == "__main__":
    print(sorted(sqn_numbers, reverse=True)[0])
    print(max(sqn_numbers))
    print(sorted(sqn_numbers)[-1])
    temp_num = 0

    for num in sqn_numbers:
        if num > temp_num:
            temp_num = num

    print(temp_num)
