
# Functional Recursion
def factorial_of_n_numbers(n):
    if n ==0 or n==1:
        return 1
    return n * factorial_of_n_numbers(n-1)


n = 5
print(factorial_of_n_numbers(n))