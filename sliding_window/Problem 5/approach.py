"""
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""


def max_fruit_in_basket(fruits: list, k: int):
    fruit_hash_map, window_start, max_fruits = dict(), 0, 0
    for window_end in range(len(fruits)):
        fruit = fruits[window_end]
        if fruit not in fruit_hash_map:
            fruit_hash_map[fruit] = 1
        else:
            fruit_hash_map[fruit] += 1
        while len(fruit_hash_map) > k:
            fruit = fruits[window_start]
            fruit_hash_map[fruit] -= 1
            if fruit_hash_map[fruit] == 0:
                del fruit_hash_map[fruit]
            window_start += 1
        max_fruits, fruits_ = get_max(window_start, max_fruits, window_end, fruits)
    print(max_fruits, fruits_)


def get_max(window_start, max_fruits, window_end, fruits):
    return max(max_fruits, window_end-window_start + 1), fruits[window_start: window_end+1]


max_fruit_in_basket(fruits=['A', 'B', 'C', 'A', 'C'], k=2)
