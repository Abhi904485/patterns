def left_down_triangle_number(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print("{} ".format(j+1), end="")
        print("\n")


n = 5
left_down_triangle_number(n)