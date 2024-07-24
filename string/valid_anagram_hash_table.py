class Solution(object):
    def isAnagram(self, s, t):
        hash_table = dict()
        if len(s) == len(t):
            for i in s:
                if i not in hash_table:
                    hash_table[i] = 1
                else:
                    hash_table[i] += 1

            for j in t:
                if j not in hash_table:
                    return False
                else:
                    hash_table[j] -= 1
                    if hash_table[j] == 0:
                        del hash_table[j]
            else:
                return 0 == len(hash_table)

        else:
            return False


if __name__ == "__main__":
    with open("/Users/abhishek/Documents/projects/python/patterns/string/valid_anagram.txt", 'r') as fr:
        content = fr.readlines()
        count = 0
        testcases = int(content[count])
        for _ in range(testcases):
            count += 1
            s, t = list(map(str, content[count].strip().split(" ")))
            o1 = Solution()
            print(o1.isAnagram(s, t))
