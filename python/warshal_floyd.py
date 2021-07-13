INF = pow(10, 9)+7
G = [[INF]*(n+1) for i in range(n+1)]
dis = [[INF]*(n+1) for i in range(n+1)]

# O(V^3)
def warshall_floyd():
    for i in range(1, n+1): dis[i][i] = 0
    for k in range(0, n+1):
        for v in range(1, n+1):
            for to in range(1, n+1):
                if(k == 0 and G[v][to] < INF): 
                    dis[v][to] = G[v][to]; continue
                # dis[v][to] = min(dis[v][to], dis[v][k]+dis[k][to])
                if(dis[v][to] > dis[v][k]+dis[k][to]):
                    dis[v][to] = dis[v][k]+dis[k][to]
                

# [ex. ABC 051 D]
#
# [input]
#
# n,m = map(int, input().split())
# G = [[INF]*(n+1) for i in range(n+1)]
# for i in range(m):       # mなので注意
#     a,b,c = map(int, input().split())
#     G[a][b] = c
#     G[b][a] = c
#
# 