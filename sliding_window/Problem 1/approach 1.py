# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# find the average of all contiguous subarrays of size ‘5’ in the given array.

# Approach First
# Analysis first for loop O(n) second for loop k times 
# Time Complexity O(n*k)

def find_average(arr: list, k: int):
    for i in range(len(arr)-k+1):
        average_sum = 0
        for j in range(i, i+k):
            average_sum += arr[j]
        print(average_sum/k)


find_average(arr=[1, 3, 2, 6, -1, 4, 1, 8, 2], k=5)
