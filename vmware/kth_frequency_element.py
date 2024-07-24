def kth_frequency(array, k):
    hash_table = dict()
    for i in array:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1
    result = []
    for value, _ in sorted(hash_table.items(), key=lambda kv: kv[1],reverse=True)[:k]:
        result.append(value)
    return result


array = [2, 2, 10, 10, 10, 3]
k = 2
kth_frequency(array, k)

output = [10, 2]
