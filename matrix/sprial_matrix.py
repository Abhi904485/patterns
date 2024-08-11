def printSpiralOrder(mat):
    # row
    top, bottom = 0, len(mat) - 1
    # column
    left, right = 0, len(mat[0]) - 1

    while True:
        if left > right:
            break

        for i in range(left, right + 1):
            print(mat[left][i], end=" ")
        top += 1

        if top > bottom:
            break

        for j in range(top, bottom + 1):
            print(mat[j][right], end=" ")
        right -= 1

        if left > right:
            break

        for k in range(right, left - 1, -1):
            print(mat[bottom][k], end=" ")
        bottom -= 1

        if top > bottom:
            break

        for l in range(bottom, top - 1, -1):
            print(mat[l][left], end=" ")
        left += 1


if __name__ == '__main__':

    mat = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]

    printSpiralOrder(mat)
