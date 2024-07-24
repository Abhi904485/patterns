def min_operation_to_convert_one_string_to_another_string(string1, string2):
    hash1 = dict()
    min_operation = 0 
    for i in string1:
        if i not in hash1:
            hash1[i] = 1
        else:
            hash1[i] += 1

    for j in string2:
        if j not in hash1:
            min_operation +=1
        else:
            hash1[j] -= 1
            if hash1[j] == 0:
                del hash1[j]

    return min_operation + sum(hash1.values())


if __name__ == "__main__":
    with open("/Users/abhishek/Documents/projects/python/patterns/string/bob_and_string.txt", 'r') as fr:
        content = fr.readlines()
        count = 0
        testcases = int(content[count])
        for _ in range(testcases):
            count += 1
            string1 = content[count].strip()
            count += 1
            string2 = content[count].strip()
            print(min_operation_to_convert_one_string_to_another_string(
                string1, string2))
