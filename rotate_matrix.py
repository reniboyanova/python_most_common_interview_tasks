def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    print(top, bottom, left, right)
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

def spiral_order2(matrix):
    result = []
    while matrix:
        result += matrix[0]
        matrix = list(zip(*matrix[1:]))[::-1]
    return result


# Тук се вижда нагледно какво се случва:
def spiral_order3(matrix):
    result = []
    while matrix:
        result += matrix[0]  # Добавяме първия ред към резултата
        matrix = matrix[1:]  # Премахваме първия ред
        if matrix and matrix[0]:  # Проверяваме дали има още редове
            matrix = list(zip(*matrix))[::-1]  # Завъртаме матрицата обратно на часовниковата стрелка
    return result

# Result:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]
    print(spiral_order(matrix))
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]

    print(spiral_order2(matrix))
