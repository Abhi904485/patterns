def another_symmtery(n):
    for i in range(n-1, -1, -1):
        #  Star
        for j in range(n-i, 0, -1):
            print("* ", end="")

        #  Space
        for k in range(i):
            print("  "*2, end="")

        #  Star
        for j in range(n-i, 0, -1):
            print("* ", end="")
        print(end="\n")
    for i in range(1, n):
        #  Star
        for j in range(n-i ,0, -1):
            print("* ", end="")

        #  Space
        for k in range(i):
            print("  "*2, end="")

        #  Star
        for j in range(n-i,0, -1):
            print("* ", end="")

        print(end="\n")

n = 3
another_symmtery(n=n)