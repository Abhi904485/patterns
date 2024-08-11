import sys


def number_of_rubies(string1):
    hash_table = dict()
    hash_table['r'] = string1.count('r', None)
    hash_table['u'] = string1.count('u', None)
    hash_table['b'] = string1.count('b', None)
    hash_table['y'] = string1.count('y', None)
    min_rubies = sys.maxsize
    for i in hash_table.values():
        if i == 0:
            min_rubies = 0
            break
        else:
            min_rubies = min(min_rubies, i)

    return min_rubies


if __name__ == "__main__":
    with open("/Users/abhishek/Documents/projects/python/patterns/string/little_jhool_and_ghost.txt", 'r') as fr:
        content = fr.readlines()
        count = 0
        testcases = int(content[count])
        for _ in range(testcases):
            count += 1
            string1 = content[count].strip()
            print(number_of_rubies(string1))
1
1
2
2
0
1
2
1
2
3