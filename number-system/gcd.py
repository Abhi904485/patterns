def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b, g):
    return (a * b) // g


M = 1e9+7


def power_exponenciation_recursive(a, b):
    if b == 0:
        return 1
    temp = power_exponenciation_recursive(a, b // 2)
    if b & 1:
        return a * temp * temp
    else:
        return temp * temp


def power_exponenciation_iterative(a, b):
    ans = 1
    while b:
        if b & 1:
            ans *= a % M
        a *= a % M
        b >>= 1
    return ans


if __name__ == "__main__":
    gcd_ = gcd(18, 12)
    print("GCD = {}".format(gcd_))
    print(lcm(18, 12, gcd_))
    print(power_exponenciation_recursive(12, 3))
    print(power_exponenciation_iterative(12, 3))
