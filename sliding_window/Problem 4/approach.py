"""
find the length of the longest substring in it with no more than K distinct characters.
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
"""

# Time Complexity O(N+N) ~ O(N)
# Space Complexity O(k+1) storing char in hashmap

def longest_substring_with_k_distinct_char(string: str, k: int):
    window_start = 0
    max_length = 0
    char_frequency = dict()
    for window_end in range(len(string)):
        char = string[window_end]
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

        while len(char_frequency) > k:
            char = string[window_start]
            char_frequency[char] -= 1
            if char_frequency[char] == 0:
                del char_frequency[char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    print(max_length)


longest_substring_with_k_distinct_char(string="araaci", k=2)
