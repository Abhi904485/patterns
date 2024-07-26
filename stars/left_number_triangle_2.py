def left_number_triangle_2(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end="")
        print(end="\n")


n= 6
left_number_triangle_2(n)