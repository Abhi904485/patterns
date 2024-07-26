def number_triangle(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1} ", end="")
        print(end="\n")


n= 5
number_triangle(n=n)