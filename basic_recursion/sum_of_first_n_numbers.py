

# Parametrized Recursion
def sum_of_first_n_numbers_pr(n, sum):
    if n == 0:
        print(sum)
        return 
    sum_of_first_n_numbers_pr(n-1, sum+n)




# Functional Recursion
def sum_of_first_n_numbers_fr(n):
    if n == 0:
        return 0
    return n+ sum_of_first_n_numbers_fr(n-1)

n =5
print(sum_of_first_n_numbers_fr(n=n))
sum_of_first_n_numbers_pr(5, 0)