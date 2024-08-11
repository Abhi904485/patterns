def left_triangle_right_triangle(n):
    for i in range(n):
        # number
        for j in range(0, i+1):
            print("{} ".format(j+1), end="")

        # space
        for l in range(2*(n-i-1), 0, -1):
            print("  ", end="")

        # number
        for k in range(i+1, 0, -1):
            print("{} ".format(k), end="")
        print(end="\n")
    

n = 4
left_triangle_right_triangle(n=n)