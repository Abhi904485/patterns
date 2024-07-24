import sys


def maximumSumSubarrayWithKElements(K, Arr, N):
        window_sum = 0
        max_sum = -sys.maxsize - 1
        start = 0
        end = N
        for window_length in range(N):
            window_sum += Arr[window_length]
            # ! Important Checking whether window length should not greator than or equal to  K-1
            if window_length>=K-1:
                max_sum = max(window_sum, max_sum)
                window_sum -= Arr[start]
                start += 1

        return max_sum
    

print(maximumSumSubarrayWithKElements(4, [1, 2, 3, 4, 5], 5))