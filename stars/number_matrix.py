def number_matrix(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top, bottom, left, right = i, 2*(n-1)-i, j, 2*(n-1)-j
            print("{}".format(n - min(top,bottom, left, right)), end="")
        print(end="\n")



n = 5
number_matrix(n=n)