# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# find the average of all contiguous subarrays of size ‘5’ in the given array.

# Approach Second
# Analysis only one for loop
# Time Complexity O(n)

def find_average(arr: list, k: int):
    window_start, window_sum = 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            print(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1


find_average(arr=[1, 3, 2, 6, -1, 4, 1, 8, 2], k=5)
