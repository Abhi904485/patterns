class Solution(object):
    def wordPattern(self, pattern, s):
        hash_table = dict()
        hash_table1 = dict()
        for i in range(len(pattern)):
            if pattern[i] not in hash_table:
                hash_table[pattern[i]] = 1
            else:
                hash_table[pattern[i]] += 1
        temp = s.split(" ")
        for j in range(len(temp)):
            if temp[j] not in hash_table1:
                hash_table1[temp[j]] = 1
            else:
                hash_table1[temp[j]] += 1
        if len(hash_table1) != len(hash_table):
            return "false"
        else:
            return "true" if list(hash_table.values()) == list(hash_table1.values()) else "false"


if __name__ == "__main__":
    with open("/Users/abhishek/Documents/projects/python/patterns/string/word_pattern.txt", 'r') as fr:
        content = fr.readlines()
        count = 0
        testcases = int(content[count])
        for _ in range(testcases):
            count += 1
            pattern = content[count].strip()
            count += 1
            string = content[count].strip()
            o1 = Solution()
            print(o1.wordPattern(pattern, string))
