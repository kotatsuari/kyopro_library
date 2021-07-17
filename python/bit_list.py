# 0~numの各bitの出現数をlistで返す
def bit_list(num, length):
    n = length
    ret = [0]*n
    for i in range(0, n):
        ret[i] = ((num+1) // (1<<(i+1))) * (1<<i)
        ret[i] += max(0, (num+1) % (1<<(i+1)) - (1<<i))
    return ret

# [sample use]

# def solution(M, N):
#     n = (N).bit_length()
#     a = bit_list(N, n)
#     b = bit_list(M-1, n)
#     res_l = [0]*n
#     for i in range(n): res_l[i] = a[i] - b[i]
#     res = 0
#     for i in range(0, n):
#         if(res_l[i] % 2 == 1): res += (1<<i)
#     return res

# N,M = map(int, input().split())
# print(solution(M,N))