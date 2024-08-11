def left_binary_triangle(n):
    for i in range(n):
        for j in range(0, i+1):
            print("{} ".format((i+j+1)%2), end="")
        print(end="\n")

n = 3
left_binary_triangle(n=n)