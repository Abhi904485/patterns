def number_of_substring_containing_all_three_distinct_chars_bf(s: str) -> int:
    count = 0
    for i in range(len(s)):
        hash_map = {}
        for j in range(i, len(s)):
            if s[j] not in hash_map:
                hash_map[s[j]] = 1
            else:
                hash_map[s[j]] += 1
            if len(hash_map) == 3:
                # did optimization here by adding len(s) - j so that if we find a substring with all three distinct characters
                # then we can add the remaining characters in the string to the count
                # So that inner loop will not run for the remaining characters in the string
                count += len(s) - j
                break
    return count


def number_of_substring_containing_all_three_distinct_chars_optimized(s: str) -> int:
    count = 0
    hash_map = {}
    right = 0
    while right < len(s):
        hash_map[s[right]] = right
        if len(hash_map) == 3:
            count += min(hash_map.values()) + 1
        right += 1

    return count


# print(number_of_substring_containing_all_three_distinct_chars_bf("aaacb"))
print(number_of_substring_containing_all_three_distinct_chars_optimized("abc"))
