def longest_repeating_char_at_most_k_replacement(s: str, k: int) -> int:
    max_length_so_far = 0
    hash_map = {}
    left = 0
    right = 0
    while right < len(s):
        if s[right] not in hash_map:
            hash_map[s[right]] = 1
        else:
            hash_map[s[right]] += 1
        max_freq = max(hash_map.values())
        #  Core Of Logic (right - left + 1) - max_freq <= k
        if (right - left + 1) - max_freq <= k:
            max_length_so_far = max(max_length_so_far, right - left + 1)
        else:
            if hash_map.get(s[left], 0):
                hash_map[s[left]] -= 1
            else:
                del hash_map[s[left]]
            left +=1
        right += 1
    return max_length_so_far


a = "ABAB"
k = 2

print(longest_repeating_char_at_most_k_replacement(a, k))
