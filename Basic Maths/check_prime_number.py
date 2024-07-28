from math import sqrt


def check_prime_number(number):
    count  = 0
    for i in range(1, int(sqrt(number)) + 1):
        if not number%i:
            count +=1
            if i != number//i:
                count +=1
        if count > 2:
            return False
    else:
        return True

n= 10
print(check_prime_number(number=n))