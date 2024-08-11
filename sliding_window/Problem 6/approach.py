"""
find the length of the longest substring which has no repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

"""


def longest_substring_no_repeating_chars(string: str):
    window_start, char_hashmap, max_length = 0, dict(), 0
    for window_end in range(len(string)):
        char = string[window_end]
        if char in char_hashmap:
            window_start = max(window_start, char_hashmap[char]+1)
        char_hashmap[char] = window_end
        max_length = max(max_length, window_end-window_start+1)
    print(max_length)


longest_substring_no_repeating_chars(string="aabccbb")
