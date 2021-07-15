# 辺に負の重みを含むときは ベルマンフォード

# O(VE) 最短経路問題　最短経路が決まるかどうかをTrue/Falseで返す
INF = pow(10, 14)+7
V = [INF]*n

def bellman_ford(s, g, V, E):
    V[s] = 0
    for i in range(n):
        for v,to,cost in E:
            if(V[to] <= V[v]+cost): continue
            V[to] = V[v] + cost
    keep = V[g]
    for i in range(n):
        for v,to,cost in E:
            if(V[to] <= V[v]+cost): continue
            V[to] = V[v] + cost
    if(keep == V[g]): return True
    else: return False

# O(VE) 最長経路問題　初期化は -INF
INF = pow(10, 14)+7
V = [-INF]*n

def bellman_ford(s, g, V, E):
    V[s] = 0
    for i in range(n):
        for v,to,cost in E:
            if(V[to] >= V[v]+cost): continue
            V[to] = V[v] + cost
    keep = V[g]
    for i in range(n):
        for v,to,cost in E:
            if(V[to] >= V[v]+cost): continue
            V[to] = V[v] + cost
    if(keep == V[g]): return True
    else: return False


# [ex. ABC 061 D]
#
# [input sample]
# n,m = map(int, input().split())
# E = [(0,0,0) for i in range(m)]
# for i in range(m): 
#     a,b,c = map(int, input().split())
#     a-=1; b-=1
#     E[i] = (a,b,c)