def left_triangle_mirror(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print(end="\n")
    for i in range(n-1, -1, -1):
        for j in range(i):
            print("* ", end="")
        print(end="\n")

n =5 
left_triangle_mirror(n=n)