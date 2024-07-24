import sys


def maxSubArraySum(arr, N):
    start = 0
    end = N
    max_so_far = -sys.maxsize - 1
    window_sum = 0
    for i in range(N):
        window_sum += arr[i]
        if max_so_far < window_sum:
            max_so_far = window_sum
            end = i

        if window_sum < 0:
            window_sum = 0

    return max_so_far, start, end


print(maxSubArraySum([-1, -2, -3, -4], 4))
