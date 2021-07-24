# 素因数分解

def prime_factorize(n):
    ret = []
    for a in range(2, int(n**0.5)+1, 1):
        if(n % a != 0): continue
        ex = 0
        while(n % a == 0):
            ex += 1
            n //= a
        ret.append([a, ex])
    if(n != 1): ret.append([n, 1])
    return ret

# 約数列挙
def enum_divisors(n):
    ret = []
    for i in range(1, int(n**0.5)+1, 1):
        if(n % i == 0):
            ret.append(i)
            if(n//i != i): ret.append(n//i)
    ret.sort()
    return ret