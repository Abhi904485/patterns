def count_elements_frequnecy_in_array(arr):
    hash_map = {}
    for i in arr:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    return hash_map


arr = [1,4,2,3,1,2,3,4,2,5]

print(count_elements_frequnecy_in_array(arr=arr))