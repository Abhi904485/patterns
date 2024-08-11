number = 6
print(f"Original number {number}")
print(f"Binary Representation of  number {bin(number)}")
unset_bit = 1
print(f"After Setting bit of number {number} is {number & ~(1<<unset_bit)}")