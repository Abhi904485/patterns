def fibonacci_tabulation(number: int, cache={0: 0, 1: 1}) -> int:
    for i in range(2, number + 1):
        cache[i] = cache[i-1]+ cache[i-2]
        cache.pop(i-2)
    return cache[number]

print(fibonacci_tabulation(4))