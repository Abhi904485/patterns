from math import sqrt

def divisors_brutebf(number):
    result = []
    for i in range(1, number+1):
        if not number%i:
            result.append(i)

    return result


def divisors_optimal(number):
    result = []
    for i in range(1, int(sqrt(number))+1):
        if number%i == 0:
            result.append(i)
            if i != number//i:
                result.append(number//i)
    return result


n = 36

print(divisors_optimal(number=n))
print(divisors_brutebf(number=n))