"""
Given an array of positive numbers and a positive number 'k', 
find the maximum sum of any contiguous subarray of size 'k'.
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]
"""
# Time Complexity O(n*k)
import sys


def max_sum_subarray(arr: list, k: int):
    max_sum = -sys.maxsize
    for i in range(len(arr)-k+1):
        current_sum = None
        for j in range(i, i+k):
            if not current_sum:
                current_sum = arr[j]
            else:
                current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
    print(max_sum)


max_sum_subarray(arr=[0, 3, 4, 1, 5], k=2)
