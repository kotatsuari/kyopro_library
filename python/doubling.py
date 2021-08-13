# ダブリング
# ある地点からk個先の要素を求める
# 初期化 O(nlogk) / クエリ O(logk)

# 入力
# n,k = map(int, input().split())
# a = list(map(lambda x: int(x)-1, input().split()))

dp = [[0]*n for i in range(k.bit_length())]
for i in range(n): dp[0][i] = a[i]
for ki in range(1, k.bit_length()): 
    for i in range(n):
        dp[ki][i] = dp[ki-1][dp[ki-1][i]]

# 出力
# res = 0
# for ki in range(k.bit_length()):
#     if(k & 1<<ki): res = dp[ki][res]
#
# [ex. ABC 167 D]