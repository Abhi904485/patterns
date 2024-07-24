from itertools import zip_longest


class Solution(object):
    def wordPattern(self, pattern, s):
        temp = s.split(" ")
        return len(set(pattern)) == len(set(temp)) == len(zip(pattern, temp))
