def pair_sum_bf(array, array_length, required_sum):
    hash_table = dict()
    for i in range(array_length):
        hash_table[array[i]] = i

    for j in range(array_length):
        if required_sum - array[j] in hash_table and j != hash_table[required_sum - array[j]]:
            return "YES"
    else:
        return "NO"

def pair_sum_optimized(array, array_length, required_sum):
    hash_table = dict()
    for i in range(array_length):
        hash_table[array[i]] = i

    for j in range(array_length):
        if required_sum - array[j] in hash_table and j != hash_table[required_sum - array[j]]:
            return "YES"
    else:
        return "NO"