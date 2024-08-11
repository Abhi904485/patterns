"""
Given a string and a pattern, 
find out if the string contains any permutation of the pattern.
"""


def find_permutation(string: str, pattern: str):
    window_start, matched = 0, 0
    char_frequency = dict()

    for char in pattern:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for window_end in range(len(string)):
        char = string[window_end]
        if char in char_frequency:
            char_frequency[char] -= 1
            if char_frequency[char] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True

        if window_end >= len(pattern)-1:
            char = string[window_start]
            window_start += 1
            if char in char_frequency:
                if char_frequency[char] == 0:
                    matched -= 1
                char_frequency[char] += 1

    return False


string = "oidbcaf"
pattern = "abc"

if find_permutation(string=string, pattern=pattern):
    print("Permutaion of pattern {} found in string {}".format(string, pattern))
else:
    print("Permutaion of pattern {} not found in string {}".format(string, pattern))
