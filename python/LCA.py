# LCA(Lowest Common Ancestor)
# 任意の２点間の最近共通祖先を求める
# 入力: グラフ G, 根の指定 root
# 初期化(__init__): O(nlogn)
# クエリ(query): O(logn)

from collections import deque
class LCA:
    def __init__(self, G, root=0):
        self.n = len(G)
        self.G = G
        self.K = self.n.bit_length()
        self.parent = [[-1]*self.n for i in range(self.K)]
        self.dist = [-1]*self.n
        self.dfs(root, -1, 0)
        for k in range(0, self.K-1, 1):
            for i in range(0, self.n, 1):
                if(self.parent[k][i] < 0): self.parent[k+1][i] = -1
                else: self.parent[k+1][i] = self.parent[k][self.parent[k][i]]

    def dfs(self, v, p, d): # １つ先の親を求める
        stack = deque()
        stack.append((-1, v, p, d))
        stack.append(( 1, v, p, d))
        while(stack):
            t,v,p,d = stack.pop()
            if(t==1):
                self.parent[0][v] = p
                self.dist[v] = d
                for to in self.G[v]:
                    if(to == p): continue
                    stack.append((-1, to, v, d+1))
                    stack.append(( 1, to, v, d+1))
            elif(t==-1):
                pass
    
    def query(self, u, v):  # 頂点u,vの最近共通祖先を求める
        if(self.dist[u] < self.dist[v]): u,v = v,u
        for k in range(0, self.K, 1):
            if((self.dist[u] - self.dist[v]) & (1<<k)):
                u = self.parent[k][u]
        if(u == v): return u
        for k in range(self.K-1, -1, -1):
            if(self.parent[k][u] != self.parent[k][v]):
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def get_dist(self, u, v):   # 任意の２点間の距離を求める
        return self.dist[u] + self.dist[v] - 2*self.dist[self.query(u, v)]    
        
    def is_on_path(self, u, v, a):  # ある頂点が任意の2点間の経路上に存在するかどうか
        return (self.get_dist(u, a) + self.get_dist(v, a)
                == self.get_dist(u, v))