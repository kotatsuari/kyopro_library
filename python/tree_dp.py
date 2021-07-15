# O(V) 木DP dp[s]に答えが入る

def merge(calcu, mi):
    ret = max(calcu, mi)
    return ret

def add_root(calcu):
    ret = calcu + 1
    return ret

def dfs(v, p=-1):
    deg = len(v)
    if(deg == 1): dp[v] = 0; return
    calcu = 0
    for to in G[v]:
        if(to == p): continue
        dfs(to, v)
        calcu = merge(calcu, dp[to])
    dp[v] = add_root(calcu)


# [ex. 036 ABC D]