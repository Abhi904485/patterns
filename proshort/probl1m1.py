# time Complexity & Space O(rows*columns)

from collections import deque


def print_ways(result, rows, columns):
    left = 0
    right = len(result[0]) - 1
    top = 0
    bottom = len(result) - 1
    for i in range(left, right + 1):
        result[left][i] = 1
    left += 1
    for j in range(top, bottom+ 1):
        result[j][top] = 1
    top += 1
    for l in range(top, bottom + 1):
        for k in range(left, right + 1):
            result[l][k] = result[l - 1][k] + result[l][k-1]
    return result


rows = 3
columns = 3
result = [[1 for _ in range(columns)]for _ in range(rows)]
print(print_ways(result, rows, columns))
