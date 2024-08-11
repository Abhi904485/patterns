def capital_letter_pyramid(n):
    for i in range(n):
        count = 65
        # space
        for j in range(n-i-1):
            print("  ", end="")
        # letter
        break_point = (2*i+1)//2
        for k in range(2*i+1):
            if k < break_point:
                print("{} ".format(chr(count)), end="")
                count +=1
            else:
                print("{} ".format(chr(count)), end="")
                count -=1
        # space
        for j in range(n-i-1):
            print("  ", end="")
        print(end="\n")

n = 3
capital_letter_pyramid(n=n)
