def rectangle_star(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1:
                print("*", end="")
            else:
                if j == 0 or j == n-1:
                    print("*", end="")
                else:
                    print(" ", end="")

        print(end="\n")


n = 5

rectangle_star(n=n)

"""
* * *
*   *
* * *
"""