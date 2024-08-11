from collections import deque


def paint_matrix(mat, x, y, new_value, old_value, visited):
    if row_start <= x <= row_end and col_start <= y <= col_end:
        if (x, y) not in visited and mat[x][y] == old_value:
            queue.append((x, y))
            while queue:
                qx, qy = queue.popleft()
                visited.append((qx, qy))
                mat[qx][qy] = new_value
                paint_matrix(mat, x, y - 1, new_value, old_value, visited)
                paint_matrix(mat, x, y + 1, new_value, old_value, visited)
                paint_matrix(mat, x - 1, y, new_value, old_value, visited)
                paint_matrix(mat, x + 1, y, new_value, old_value, visited)
    else:
        return


if __name__ == '__main__':

    mat = [
        [0, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 1, 0, 0],

    ]
    x = 0
    y = 2
    queue = deque()
    visited = []
    previous_value = mat[x][y]
    row_start, row_end = 0, len(mat) - 1
    col_start, col_end = 0, len(mat[0]) - 1
    paint_matrix(mat, x, y, 2, previous_value, visited)
    print(mat)
