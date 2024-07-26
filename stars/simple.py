"""
* * *
* * *
* * *
"""

def simple(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print(end="\n")

n =6
simple(n)