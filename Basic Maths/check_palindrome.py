def check_palindrome(n):
    temp = n
    result = 0
    while n>0:
        result = (result*10) + n%10
        n //=10
    return result == temp

n = 121
print(check_palindrome(n))