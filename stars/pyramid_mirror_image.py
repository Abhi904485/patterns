def pyramid_mirror_image(n):
    for i in range(n):
        for k in range(n-(i+2), -1, -1):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for l in range(n-(i+2), -1, -1):
            print("", end="")
        print("\n")
    for i in range(n-1, -1, -1):
        for k in range(n-(i+2), -1, -1):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for l in range(n-(i+2), -1, -1):
            print(" ", end="")
        print("\n")

n = 3
pyramid_mirror_image(n =n)