def fibonacci_memoization(number: int, cache={}) -> int:
    if number in cache:
        return cache[number]
    if number == 0:
        return 0
    if number == 1:
        return 1
    result = fibonacci_memoization(
        number - 2) + fibonacci_memoization(number - 1)
    cache[number] = result
    return result


fibonacci_memoization(11)
