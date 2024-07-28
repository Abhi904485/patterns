def gcd_or_hcf_bf(n1, n2):
    n1_factors = set()
    n2_factors = set()
    for i in range(1, n1+1):
        if n1%i == 0:
            n1_factors.add(i)
    for j in range(1, n2+1):
        if n2%j == 0:
            n2_factors.add(j)
    return max(n1_factors.intersection(n2_factors))

# T(n) O(2n)
# S(n) O(1)


def gcd_or_hcf_optimized_1(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2)):
        if n1%i == 0  and n2%i == 0:
            gcd = i
    return gcd

# T(n) min(O(n1), O(n2))
# S(n) O(1)

def gcd_or_hcf_optimized_2(n1, n2):
    gcd = 1
    for i in range(min(n1, n2), 0, -1):
        if n1%i == 0  and n2%i == 0:
            return i
    return gcd

# T(n) min(O(n1), O(n2))
# S(n) O(1)

def gcd_or_hcf_optimal_recursive(n1, n2):
    if n1 == 0:
        return n2
    return gcd_or_hcf_optimal_recursive(n2%n1, n1)

# Time Complexity: O(Log min(a, b))
# Auxiliary Space: O(Log (min(a,b))

def gcd_or_hcf_optimal_iterative1(n1, n2):
    while n1>0 and n2>0:
        if n1>n2:
            n1 = n1%n2
        else:
            n2 =  n2%n1
    if n1 == 0:
        return n2
    return n1
    
def gcd_or_hcf_optimal_iterative2(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1


n1 = 98
n2 = 56

print(gcd_or_hcf_bf(n1=n1, n2=n2))
print(gcd_or_hcf_optimized_1(n1=n1, n2=n2))
print(gcd_or_hcf_optimized_2(n1=n1, n2=n2))
print(gcd_or_hcf_optimal_recursive(n1=n1, n2=n2))
print(gcd_or_hcf_optimal_iterative1(n1=n1, n2=n2))
print(gcd_or_hcf_optimal_iterative2(n1=n1, n2=n2))
