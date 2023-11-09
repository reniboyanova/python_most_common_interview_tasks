matrix_to_rotate = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]


def rotate_matrix(matrix):
    matrix = list(zip(*matrix[::-1]))
    return matrix


def rotate_matrix2_reni(matrix):
    matrix_to_return = []
    row = len(matrix[0]) - 1
    len_matrix = len(matrix)
    cow = 0

    for _ in range(len_matrix):
        list_to_append = []
        for i in range(len_matrix):
            list_to_append.append(matrix[row][cow])
            row -= 1
        cow += 1
        matrix_to_return.append(list_to_append)
        row = len(matrix[0]) - 1

    return matrix_to_return

def rotate_matrix_3_reni(matrix):
    matrix_to_return = []
    while matrix:
        for row in range(len(matrix) - 1, -1, -1):
            matrix_to_return.append(matrix.pop(row))

    matrix_to_return = [list(row) for row in (zip(*matrix_to_return))]
    return matrix_to_return


if __name__ == "__main__":
    # matrix_to_rotate = rotate_matrix(matrix_to_rotate)
    #
    # for i in matrix_to_rotate:
    #     print(list(i))

    # matrix_to_rotate_2 = rotate_matrix2_reni(matrix_to_rotate)
    # for i in matrix_to_rotate_2:
    #     print(i)

    matrix_to_rotate = rotate_matrix_3_reni(matrix_to_rotate)
    print('\n'.join(map(str, matrix_to_rotate)))
