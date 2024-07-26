def left_reverse_capital_alphabet(n):
    count  = 65+n
    for i in range(n):
        count -=1
        for j in range(i+1):
            print("{} ".format(chr(count+j)), end="")
        print("\n")



n = 5
left_reverse_capital_alphabet(n=n)