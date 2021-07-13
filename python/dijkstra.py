G = [[] for i in range(n)]
INF = pow(10,9)+7
dis = [INF]*n

# O(V^2) queueのダイクストラ
from collections import deque
def dijkstra(s, dis, G):
    d = deque()
    d.append((s,0))
    dis[s] = 0
    while(d):
        v,cost = d.popleft()
        if(dis[v] < cost): continue
        for to,time in G[v]:
            if(dis[to] <= dis[v]+time): continue
            dis[to] = dis[v] + time
            d.append((to, dis[to]))

# O(ElogV) priority queueのダイクストラ (vとcostの位置が逆なので注意)
import heapq
def dijkstra(s, dis, G):
    pq = []
    heapq.heappush(pq, (0,s))
    dis[s] = 0
    while(pq):
        cost,v = heapq.heappop(pq)
        if(dis[v] < cost): continue
        for to,time in G[v]:
            if(dis[to] <= dis[v]+time): continue
            dis[to] = dis[v] + time
            heapq.heappush(pq, (dis[to], to))

# [ex. ABC 035 D]