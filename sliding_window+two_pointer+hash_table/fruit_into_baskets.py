def max_fruit_into_baskets(arr, k):
    left = 0
    right = 0
    max_fruits_so_far = 0
    fruit_count = {}
    while right < len(arr):
        if arr[right] not in fruit_count:
            fruit_count[arr[right]] = 1
        else:
            fruit_count[arr[right]] += 1
        if len(fruit_count) > k:
            if arr[left] in fruit_count and fruit_count[arr[left]] > 0:
                fruit_count[arr[left]] -= 1
            if fruit_count[arr[left]] == 0:
                del fruit_count[arr[left]]
            left += 1
        else:
            max_fruits_so_far = max(max_fruits_so_far, right - left + 1)
        right += 1
    return max_fruits_so_far


fruits = [1, 2, 1]
k = 2
print(max_fruit_into_baskets(fruits, k))
