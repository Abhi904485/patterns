def left_capital_letter_triangle_with_every_row_same(n):
    count  = 65
    for i in range(n):
        for j in range(i+1):
            print("{} ".format(chr(count)), end="")
        count +=1
        print(end="\n")
        




n =3 

left_capital_letter_triangle_with_every_row_same(n=n)