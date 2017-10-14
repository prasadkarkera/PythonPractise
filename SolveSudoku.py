def solve_sudoku(matrix):

    row_index, col_index = find_next_unassigned_location(matrix)

    if row_index is None or col_index is None:
        return True

    for i in range(1, 10):

        if is_safe(matrix, row_index, col_index, i):
            matrix[row_index][col_index] = i

            if solve_sudoku(matrix):
                return True

            matrix[row_index][col_index] = 0

    return False


def find_next_unassigned_location(matrix):
    for row_index in range(9):
        for col_index in range(9):
            if matrix[row_index][col_index] == 0:
                return row_index, col_index

    return None, None


def is_safe(matrix, row_index, col_index, digit):

    if not_present_in_row(matrix, row_index, digit) \
        and not_present_in_column(matrix, col_index, digit) \
         and not_present_in_box(matrix, row_index- row_index%3, col_index-col_index%3, digit):
        return True
    return False


def not_present_in_box(matrix, start_row_index, start_col_index, digit):
    for i in range(3):
        for j in range(3):
            if matrix[start_row_index + i][start_col_index + j] == digit:
                return False
    return True


def not_present_in_row(matrix, row_index, digit):
    for col_index in range(9):
        if matrix[row_index][col_index] == digit:
            return False
    return True


def not_present_in_column(matrix, col_index, digit):
    for row_index in range(9):
        if matrix[row_index][col_index] == digit:
            return False
    return True


matrix = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]];

solve_sudoku(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print(matrix[4])
print(matrix[5])
print(matrix[6])
print(matrix[7])
print(matrix[8])

