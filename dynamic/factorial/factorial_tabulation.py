def fact_tabulation(number: int) -> int:
    cache = [1] * (number+1)
    for i in range(2, number + 1):
        cache[i] = i * cache[i - 1]
    return cache[-1]


print(fact_tabulation(4))
