def left_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print(end="\n")

n = 3
left_triangle(n)