def left_down_triangle(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print("*", end="")
        print("\n")


n = 5
left_down_triangle(n)