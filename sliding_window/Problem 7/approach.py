"""
Given a string with lowercase letters only, 
if you are allowed to replace no more than K letters with any letter,
find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


def length_of_longest_substring_with_k_replacement_char(string: str, k: int):
    window_start,  max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = dict()
    for window_end in range(len(string)):
        char = string[window_end]
        if char not in frequency_map:
            frequency_map[char] = 1
        else:
            frequency_map[char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[char])
        if (window_end-window_start+1 - max_repeat_letter_count) > k:
            char = string[window_start]
            frequency_map[char] -= 1
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    print(max_length)


length_of_longest_substring_with_k_replacement_char(string="aabccbb", k=2)
