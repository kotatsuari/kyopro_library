# MOD に置ける a の逆元を求める

def modinv(a, MOD):
    b = MOD; u = 1; v = 0
    while(b):
        t = a//b
        a -= t*b; a,b = b,a
        u -= t*v; u,v = v,u
    u %= MOD
    if(u < 0): u += MOD
    return u


# [ex. ABC 156 D]
#
#
# [sample] n が大きいときに COM(n,k) を求める
#
# def COM(n, k, MOD=pow(10,9)+7): 
#     ret = 1
#     waru = 1
#     for i in range(0, k):
#         ret *= (n-i)
#         ret %= MOD
#         waru *= (i+1)
#         waru %= MOD
#     ret *= modinv(waru, MOD)
#     ret %= MOD
#     return ret