def fact_memoization(number: int) -> int:
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fact_memoization(number - 1) * number


print(fact_memoization(20))
