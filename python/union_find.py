# UnionFind
# 各ノードが同じグループに属するか判定 or グループのサイズを返す
# 入力 : ノード数 n

# サイズver.
class UnionFind:    
    def __init__(self, n): # 初期化
        self.parent = list(range(0,n))
        self.size = [1]*n

    def root(self, x):  # ノード x の根を返す / 経路圧縮で  O(logn) 
        if(self.parent[x] == x): return x
        else: self.parent[x] = self.root(self.parent[x]); return self.parent[x]

    def merge(self, x, y): # ノード x,y が同じ木に属するか判定 / O(logn)
        x = self.root(x)
        y = self.root(y)
        if(x == y): return False
        if(self.size[x] > self.size[y]): x,y = y,x
        self.parent[x] = y
        self.size[y] += self.size[x]
        return True

    def isSame(self, x, y): # ノード x,y が同じ木に属するか判定 / O(logn)
        return (self.root(x) == self.root(y))

    def isSize(self, x):    # ノード x が属する木のサイズを返す
        return self.size[self.root(x)]


# なんでか知らんけどちょっと早いver.
class UnionFind:
    def __init__(self,n):
        self.par = [-1]*n
    def root(self, x):
        if(self.par[x] < 0): return x
        else: self.par[x] = self.root(self.par[x]); return self.par[x]
    def same(self, x, y):
        return (self.root(x) == self.root(y))
    def merge(self, x, y):
        x = self.root(x); y = self.root(y)
        if(x == y): return False
        if(self.par[x] > self.par[y]): x,y = y,x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True
    def size(self, x):
        return -self.par[self.root(x)]


# [ex. ABC 214 D]