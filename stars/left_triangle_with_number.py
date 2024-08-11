def left_triangle_with_increasing_number(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            count += 1
            print("{} ".format(count), end="")
        print(end="\n")


left_triangle_with_increasing_number(n=3)
