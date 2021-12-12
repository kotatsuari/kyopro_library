class Bipartite_Matching:
    def __init__(self, n1, n2):     # グループ 1 と 2 のマッチング
        self.n1 = n1
        self.n2 = n2
        self.n = 1 + n1 + n2 + 1
        self.G = [[] for i in range(self.n)]
        self.INF = pow(10,9)+7
        self.used = [False]*self.n
        self.start = 0
        self.goal = self.n - 1
        for i in range(1, n1+1):
            self.add_edge(self.start, i, 1)
        for j in range(n1+1, self.n-1):
            self.add_edge(j, self.goal, 1)

    def flow_dfs(self, v, t, mincap):   # __ 目的の頂点 t にたどり着くまでの最小容量を求め、通って来た辺に流して帰る
        if(v == t): return mincap
        self.used[v] = True
        for edge in self.G[v]:
            to,cap,rev = edge[0],edge[1],edge[2]
            if(not self.used[to] and cap > 0):
                d = self.flow_dfs(to, t, min(mincap, cap))
                if(d > 0):
                    edge[1] -= d
                    self.G[to][rev][1] += d
                    return d
        return 0

    def max_flow(self, s, t):   # __ 頂点 s から t の最大流を求める
        flow = 0
        while(1):
            self.used = [False]*self.n
            f = self.flow_dfs(s, t, self.INF)
            if(f == 0): return flow
            flow += f

    def add_edge(self, From, to, cap):  # __ 辺を追加
        self.G[From].append([to, cap, len(self.G[to])])
        self.G[to].append([From, 0, len(self.G[From])-1])

    def add(self, i, j):    # グループ 1の i番目からグループ 2の j番目への辺を追加
        From = 1 + i
        to = 1 + self.n1 + j
        self.G[From].append([to, 1, len(self.G[to])])
        self.G[to].append([From, 0, len(self.G[From])-1])

    def solve(self):        # グループ 1からグループ 2への最大マッチング結果を出力
        return self.max_flow(self.start, self.goal)

# [ex. ARC 092 C]
# [sample.]
# n = int(input())
# a = [0]*n; b = [0]*n
# c = [0]*n; d = [0]*n
# for i in range(n):
#     ai,bi = map(int, input().split())
#     a[i],b[i] = ai,bi
# for i in range(n):
#     ci,di = map(int, input().split())
#     c[i],d[i] = ci,di

# bm = Bipartite_Matching(n, n)
# for i in range(n):
#     for j in range(n):
#         if(a[i] < c[j] and b[i] < d[j]): bm.add(i, j)

# print(bm.solve())
