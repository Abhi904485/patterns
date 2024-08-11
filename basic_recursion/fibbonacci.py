def fibbonacci_iterative(n):
    a = 0
    b = 1
    print(a, end =" ")
    for _ in range(1, n+1):
        print(b, end=" ")
        a, b = b, a+b
    print(end="\n")
        

def fibbonacci_recursive(n):
    if n <=1:
        return n
    return fibbonacci_recursive(n-1)+ fibbonacci_recursive(n-2)


def fibboanci_tabulization_optimization(n):
    cache = {0: 0, 1: 1}
    print(cache[0], end=" ")
    print(cache[1], end=" ")
    for i in range(2, n):
        cache[i] = cache[i-1] + cache[i-2]
        print(cache[i], end=" ")
    print(end="\n")


def fibboanci_memoization_optimization(n, cache={0:0, 1:1}):
    if n in cache:
        return cache[n]
    cache[n] = fibboanci_memoization_optimization(n-1) + fibboanci_memoization_optimization(n-2)
    print(cache[n], end=" ")
    return cache[n]

     

n = 5

# Iterative callee
fibbonacci_iterative(n)
# Recursive Callee
for i in range(n+1):
    print(fibbonacci_recursive(i), end=" ")
print(end="\n")

# With Dynamic programming bottom up approach
fibboanci_tabulization_optimization(n+1)

# With Dynamic programming Top Down approach
print(fibboanci_memoization_optimization(n))