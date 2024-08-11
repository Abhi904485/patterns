def print_1_to_n(number):
    if number == 0:
        return
    print(f"{number} ", end="")
    print_1_to_n(number-1)
    

#  if we move line 5 before line 4 then number will print in reverse order
#  if print is on line number 5 then number will print in assending order



n = 5

print_1_to_n(number=n)