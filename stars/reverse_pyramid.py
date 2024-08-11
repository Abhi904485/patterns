def reverse_pyramid(n):
    for i in range(n-1, -1, -1):
        for k in range(n-(i+2), -1, -1):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for l in range(n-(i+2), -1, -1):
            print(" ", end="")
        print("\n")


reverse_pyramid(n =3)