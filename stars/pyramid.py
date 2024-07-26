def pyramid(n):
    for i in range(n):
        for k in range(n-i-1, -1, -1):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for l in range(n-i-1, -1, -1):
            print("", end="")
        print("\n")


pyramid(n =7)