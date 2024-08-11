"""
Given an array containing 0s and 1s, if you are allowed to replace no more than K 1s with 0s,
find the length of the longest contiguous subarray having all 0s.
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '1' at index 1 and 2 to have the longest contiguous subarray of 0s having length 6.
"""


def longest_contiguous_of_zeros(arr: list, k: int):
    window_start, max_length, max_zero_count = 0, 0, 0
    for window_end in range(len(arr)):
        element = arr[window_end]
        if element == 0:
            max_zero_count += 1

        if (window_end - window_start+1-max_zero_count) > k:
            element = arr[window_start]
            if element == 0:
                max_zero_count -= 1
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    print(max_length)


longest_contiguous_of_zeros(arr=[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],  k=2)
