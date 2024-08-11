"""
Given an array of positive numbers and a positive number S, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greator than or equal to '7' is [5, 2].

"""

import math


def smallest_subarray(arr: list, s: int):
    window_start, window_length, window_sum = 0, math.inf, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            window_length = min(window_length, window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1

    if window_length == math.inf:
        return 0
    return window_length


print(smallest_subarray(arr=[2, 1, 5, 2, 3, 2], s=7))
