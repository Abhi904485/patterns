def max_consecutive_ones_atmost_2_zero_flips(arr, k):
    left = 0
    right = 0
    max_length_so_far = 0
    zero_count = 0
    while right < len(arr):
        if arr[right] == 0:
            zero_count += 1
        if zero_count > k:
            if arr[left] == 0:
                zero_count -= 1
            left += 1
        else:
            max_length_so_far = max(max_length_so_far, right - left + 1)
        right += 1
    return max_length_so_far


arr = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3

print(max_consecutive_ones_atmost_2_zero_flips(arr, k))
