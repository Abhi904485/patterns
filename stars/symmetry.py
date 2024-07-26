def symmetry(n):
    for i in range(n):
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
    
n = 6
symmetry(n=n)