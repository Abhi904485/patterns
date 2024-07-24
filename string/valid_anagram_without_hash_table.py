class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        else:
            return True


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
