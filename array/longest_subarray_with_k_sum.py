#  BF with Time Complexity O(n^3)
def longest_subarray_with_k_sum_bf_n3(arr, k):
    max_length_subarray_so_far = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray_sum = sum(arr[i : j + 1])
            if subarray_sum == k:
                max_length_subarray_so_far = max(max_length_subarray_so_far, j - i + 1)
    return max_length_subarray_so_far


#  BF with Time Complexity O(n^2)
def longest_subarray_with_k_sum_bf_n2(arr, k):
    max_length_subarray_so_far = 0
    for i in range(len(arr)):
        subarray_sum = 0
        for j in range(i, len(arr)):
            subarray_sum += arr[j]
            if subarray_sum == k:
                max_length_subarray_so_far = max(max_length_subarray_so_far, j - i + 1)
    return max_length_subarray_so_far


#  BF with Time Complexity O(n) Space Complexity O(n)
# this will not work for negaives and Zeros For input (2,0,0,3) Actual is 1 but expected is 3
def longest_subarray_with_k_sum_better_n(arr, k):
    max_length_subarray_so_far = 0
    prefix_sum = 0
    hash_map = {}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        hash_map[prefix_sum] = i
        if prefix_sum == k:
            max_length_subarray_so_far = i + 1
        else:
            if (prefix_sum - k) in hash_map:
                max_length_subarray_so_far = max(
                    max_length_subarray_so_far, abs(hash_map[prefix_sum - k] - i)
                )

    return max_length_subarray_so_far


#  BF with Time Complexity O(n) Space Complexity O(n)
#  This will work for negaives and Zeros other as well
#  This will be the optimal if array contains negatives and zeros
def longest_subarray_with_k_sum_better_n_with_zero_and_negatives(arr, k):
    max_length_subarray_so_far = 0
    prefix_sum = 0
    hash_map = {}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum not in hash_map:
            hash_map[prefix_sum] = i
        if prefix_sum == k:
            max_length_subarray_so_far = i + 1
        else:
            if (prefix_sum - k) in hash_map:
                max_length_subarray_so_far = max(
                    max_length_subarray_so_far, abs(hash_map[prefix_sum - k] - i)
                )

    return max_length_subarray_so_far


#  This will be the optimal if array contains only postives and zeros without hashing
def longest_subarray_with_k_sum_optimized(arr, k):
    max_length_subarray_so_far = 0
    left, right = 0, 0
    prefix_sum = arr[0]
    while right < len(arr):
        while prefix_sum > k and left <= right:
            prefix_sum -= arr[left]
            left +=1
        if prefix_sum == k:
            max_length_subarray_so_far = max(max_length_subarray_so_far, right-left+1)
        right += 1
        #  here below condition is for handling for list out of bound exception
        if right < len(arr):
            prefix_sum += arr[right]
    return max_length_subarray_so_far



# print(
#     longest_subarray_with_k_sum_better_n_with_zero_and_negatives(
#         [1, 2, 3, 1, 1, 1, 1, 3, 3], 6
#     )
# )

print(
    longest_subarray_with_k_sum_optimized(
        [1, 2, 1, 3], 2
    )
)
