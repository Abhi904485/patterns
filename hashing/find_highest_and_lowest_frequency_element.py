arr = [2, 2, 3, 4, 4]


def find_highest_lowest_frequency_element(arr):
    hash_map = {}
    start = 0
    end = len(arr) - 1
    if len(arr)%2 == 0:
        while start < end:
            if arr[start] in hash_map:
                    hash_map[arr[start]] += 1
            else:
                hash_map[arr[start]] = 1
            if arr[end] in hash_map:
                hash_map[arr[end]] += 1
            else:
                hash_map[arr[end]] = 1
            start +=1
            end -=1
    else:
        while start < end:
            if arr[start] in hash_map:
                    hash_map[arr[start]] += 1
            else:
                hash_map[arr[start]] = 1
            if arr[end] in hash_map:
                hash_map[arr[end]] += 1
            else:
                hash_map[arr[end]] = 1
            start +=1
            end -=1
        else:
            if arr[start] in hash_map:
                    hash_map[arr[start]] += 1
            else:
                hash_map[arr[start]] = 1
    max_freq_so_far, min_freq_so_far = 0, len(arr)
    max_freq_element, min_freq_element = 0, 0
    for key, freq in hash_map.items():
        if freq > max_freq_so_far:
            max_freq_so_far = max(max_freq_so_far, freq)
            max_freq_element = key
        else:
            if freq < min_freq_so_far:
                min_freq_so_far = min(min_freq_so_far, freq)
                min_freq_element = key
    return max_freq_element, min_freq_element


print(find_highest_lowest_frequency_element(arr=arr))
