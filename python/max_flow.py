# ------------
n,g,e = map(int, input().split())
p = map(int, input().split())
G = [[] for i in range(n)]
for i in range(e):
    a,b = map(int, input().split())
    G[a].append([b, 1, len(G[b])])
    G[b].append([a, 0, len(G[a])-1])

INF = pow(10,9)+7
# --------------

# vからtまで流す
def flow_dfs(v, t, mincap, used):
    if(v == t): return mincap
    used[v] = True
    for edge in G[v]:
        to,cap,rev = edge[0],edge[1],edge[2]
        # print(to, cap, rev)
        if(not used[to] and cap > 0):
            d = flow_dfs(to, t, min(mincap, cap), used)
            if(d > 0):
                edge[1] -= d
                G[to][rev][1] += d
                return d
    return 0

# sからtまでの最大流を求める
def max_flow(s, t):
    flow = 0
    while(1):
        used = [False]*n
        f = flow_dfs(s, t, INF, used)
        if(f == 0): return flow
        flow += f


print(max_flow(0, n-1))