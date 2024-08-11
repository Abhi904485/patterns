def getMinDiff(arr, n, k):
    for i in range(n):
        if arr[i] - k > 0:
            arr[i] = arr[i] - k
        elif arr[i] - k < 0:
            arr[i] = arr[i] + k
    arr.sort()
    return arr[-1] - arr[0]


print(getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 10, 5))
