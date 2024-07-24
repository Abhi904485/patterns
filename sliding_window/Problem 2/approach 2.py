"""
Given an array of positive numbers and a positive number 'k', 
find the maximum sum of any contiguous subarray of size 'k'.
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]
"""
# Time complexity O(n)

import sys


def max_sum_subarray(arr: list, k: int):
    window_start, window_sum = 0, None
    max_sum = -sys.maxsize
    for window_end in range(len(arr)):
        if not window_sum:
            window_sum = arr[window_end]
        else:
            window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    print(max_sum)


max_sum_subarray(arr=[0, 3, 4, 1, 5], k=2)
max_sum_subarray(arr=[2, 1, 5, 1, 3, 2], k=3)
