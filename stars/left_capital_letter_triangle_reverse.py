def left_capital_letter_triangle_reverse(n):
    for i in range(n, -1, -1):
        count = 65
        for j in range(i):
            print("{} ".format(chr(count)), end="")
            count += 1
        print("\n")

n = 3

left_capital_letter_triangle_reverse(n=n)
