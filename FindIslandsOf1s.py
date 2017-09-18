# http://www.geeksforgeeks.org/find-number-of-islands/


def are_ids_valid(matrix, row_id, col_id):
    if  -1 < row_id < len(matrix) and -1 < col_id < len(matrix[0]):
        return True
    else:
        return False


def DFS(matrix, row_id, col_id, visited):
    row_numbers_of_neighbours = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_numbers_of_neighbours = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[f'{row_id}{col_id}'] = 1

    # loop for neighbours
    for i in range(8):
        neighbour_row_id = row_id + row_numbers_of_neighbours[i]
        neighbour_col_id = col_id + col_numbers_of_neighbours[i]
        if are_ids_valid(matrix, neighbour_row_id, neighbour_col_id):
            neighbour = matrix[neighbour_row_id][neighbour_col_id]

            if neighbour and visited.get(f'{neighbour_row_id}{neighbour_col_id}') is None:
                DFS(matrix, neighbour_row_id, neighbour_col_id, visited)


def find_islands(matrix):
    visited = {}
    count = 0
    for row_id in range(len(matrix)):
        for col_id in range(len(matrix[row_id])):
            if visited.get(f'{row_id}{col_id}') is None and matrix[row_id][col_id]:
                DFS(matrix, row_id, col_id, visited)
                count = count + 1

    return count


def main():
    matrix = [[1, 1, 0, 0, 0],
              [0, 1, 0, 0, 1],
              [1, 0, 0, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1]]

    count = find_islands(matrix)
    print(f'The number of islands = {count}')


if __name__ == '__main__':
    main()
