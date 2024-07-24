

def subArraySum(arr, n, s):
    start, end = 0, n
    window_sum = 0
    for i in range(n):
        if window_sum == s:
            if i == 0:
                return -1
            return start + 1, i
        elif window_sum < s:
            window_sum += arr[i]
        while window_sum > s:
            window_sum -= arr[start]
            start += 1
    if window_sum == s:
        return start + 1, i + 1
    else:
        return -1


print(subArraySum([1, 2, 3, 4], 5, 0))
