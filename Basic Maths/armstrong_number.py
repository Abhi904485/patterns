def check_armstrong_number(number):
    result = 0
    temp1 = number
    temp =0
    while number:
        temp = number%10
        result += temp**3
        number //=10
    if result == temp1:
        return True
    return False


number = 153

print(check_armstrong_number(number=number))