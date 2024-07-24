def max_subarray_sum(array):
    max_so_far = array[0]
    current_sum = 0
    for i in array:
        if current_sum < 0:
            current_sum = 0
        current_sum += i
        max_so_far = max(max_so_far, current_sum)
    return max_so_far
