def check_double(string):
    hash_map = dict()
    for item in string:
        if item not in hash_map:
            hash_map[item] = 1
        else:
            hash_map[item] += 1
    even_count = 0
    for i in hash_map.values():
        if i % 2 == 0 or i > 2:
            return "Yes"
    else:
        return "No"
            


if __name__ == "__main__":
    test_cases = int(input())
    for case in range(test_cases):
        string = input()
        print(check_double(string))
