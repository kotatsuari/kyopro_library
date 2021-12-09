class CSS():
    def __init__(self, n, G):
        self.n = n
        self.G = G      # normal_graph
        self.G_ = [[] for i in range(n)]    # reversed_graph
        self.compo = [-1]*n     # 頂点が属するグループ
        self.rnkt = [[]]        # 各連結グループごとの要素
        self.order = []         # dfsの順番
        self.used = [False]*n   # dfsで見たかどうか

        for v in range(n):      # 辺を反転させたグラフを作成
            for to in self.G[v]:
                self.G_[to].append(v)
    
    def operator(self, k):
        return self.compo[k]

    def dfs(self, now): # 帰りがけ順を保存
        if(self.used[now]): return
        self.used[now] = True
        for to in self.G[now]: 
            self.dfs(to)
        self.order.append(now)

    def rdfs(self, now, count): # 帰りが遅いほうから見ていく
        if(self.compo[now] != -1): return 
        self.compo[now] = count
        self.rnkt[count].append(now)
        for to in self.G_:
            self.rdfs(to, count)
    
    def build(self):
        for i in range(self.n):
            self.dfs(i)
        self.order.reverse()
        group = 0
        for i in self.order:
            if(self.compo[i] == -1):
                self.rdfs(i, group)
                group += 1
        

        ret = [[] for i in range(group)]     # まとめたグラフ
        for i in range(self.n):
            for to in self.G[i]:
                s = self.compo[i]
                t = self.compo[to]
                if(s != t): ret[s].append(t)

        return ret
    
    def rnkt(self): # 各グループに属する要素
        return self.rnkt
    



