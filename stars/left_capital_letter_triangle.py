def left_capital_letter_triangle(n):
    for i in range(n):
        count = 65
        for j in range(i + 1):
            print("{} ".format(chr(count)), end="")
            count += 1
        print("\n")

n = 3

left_capital_letter_triangle(n=n)
