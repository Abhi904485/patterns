# Longest Substring Without Repeating Characters Given a string s, 
# find the length of the longest  substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

string = " "
hash_map = {}


def check_hash_map(chr):
    return chr in hash_map


def update_hash_map(chr, chr_index):
    hash_map[chr] = chr_index

def length_of_longest_substring_without_repetiting_characters(string):
    max_length_so_far = 0
    left = 0
    right = 0
    while right < len(string):
        if not check_hash_map(string[right]):
            update_hash_map(string[right], right)
        else:
            if hash_map[string[right]] < left:
                update_hash_map(string[right], right)
            else:
                left = hash_map[string[right]] + 1
                update_hash_map(string[right], right)
        max_length_so_far = max(right-left+1, max_length_so_far)
        right += 1
    return max_length_so_far


print(length_of_longest_substring_without_repetiting_characters(string))