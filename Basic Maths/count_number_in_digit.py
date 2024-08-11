from math import log10


def count_number_in_digit_bf(n):
    count = 0
    while n>0:
        n //= 10
        count +=1
    return count

def count_number_in_digit_optimized(n):
    return int(log10(n)+1)

print(count_number_in_digit_bf(12345))
print(count_number_in_digit_optimized(12345))