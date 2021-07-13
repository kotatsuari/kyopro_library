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