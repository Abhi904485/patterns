# Number of Subarrays with Sum K


def number_of_subarrays_with_k_sum_bf(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray_sum = sum(arr[i : j + 1])
            if subarray_sum == k:
                count += 1
    return count

def number_of_subarrays_with_k_sum_optimized(arr, k):
    count = 0
    for i in range(len(arr)):
        pass
    return count


arr = [1, 2, 3]
k = 3
print(number_of_subarrays_with_k_sum_bf(arr, k))
