# 普通のセグ木（一点更新）
class SegTree:  # func で抽象化
    def __init__(self, a_list, func, ide_ele):
        n = len(a_list)
        self.func = func # 区間で行う操作関数
        self.ide_ele = ide_ele # 単位元
        self.num = 1 << (n-1).bit_length()
        self.dat = [ide_ele]*2*self.num
        for i in range(0, n): self.dat[self.num-1 + i] = a_list[i]
        for i in range(self.num-2, -1, -1):
            self.dat[i] = self.func(self.dat[2*i+1], self.dat[2*i+2])

    def update(self, i, x):
        i += self.num-1
        self.dat[i] = x # 葉の更新方法
        while(i > 0):
            i = (i-1)//2
            self.dat[i] = self.func(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, l, r): # 半開区間で考える
        res = self.ide_ele
        l += self.num-1; r += self.num-1
        while(l < r):
            if(not l & 1): res = self.func(res, self.dat[l])
            if(not r & 1): res = self.func(res, self.dat[r-1]); r-=1
            l //= 2; r //= 2
        return res

# [sample_func] 最小値を求める
# def func(x, y):
#     return min(x, y)

# 配列の番号が i であるブロックの左下のブロックの番号は 2i+1
# 　　　　　　　〃 　　　　　　　右下のブロックの番号は 2i+2
# 　　　　　　　〃　 　　　　　　上のブロックの番号は (i-1)//2
# 
# ide_ele は単位元　その値によって結果が変わらないもの（ min なら INF）


# 遅延セグ木（区間更新）
from collections import deque
class SegTree:  # func で抽象化
    def __init__(self, a_list, func, ide_ele):
        n = len(a_list)
        self.func = func # 区間で行う操作関数
        self.ide_ele = ide_ele # 単位元
        self.num = 1 << (n-1).bit_length()
        self.dat = [ide_ele]*2*self.num
        self.lazy = [ide_ele]*2*self.num
        for i in range(0, n): self.dat[self.num-1 + i] = a_list[i]
        for i in range(self.num-2, -1, -1):
            self.dat[i] = self.func(self.dat[2*i+1], self.dat[2*i+2])

    def eval(self, k):
        if(self.lazy[k] == self.ide_ele): return 
        if(k < self.num-1):
            self.lazy[k*2 + 1] = self.lazy[k]
            self.lazy[k*2 + 2] = self.lazy[k]
        self.dat[k] = self.lazy[k]
        self.lazy[k] = self.ide_ele

    # def update_sub(self, a, b, x, k, l, r):
    #     self.eval(k)
    #     if(a <= l and r <= b):
    #         self.lazy[k] = x
    #         self.eval(k)
    #     elif(a < r and l < b):
    #         self.update_sub(a, b, x, k*2 + 1, l, (l+r)//2)
    #         self.update_sub(a, b, x, k*2 + 2, (l+r)//2, r)
    #         self.dat[k] = self.func(self.dat[k*2 + 1], self.dat[k*2 + 2])

    def update_sub(self, a, b, x, k, l, r):
        d = deque()
        d.append((-1, a, b, x, k, l, r))
        d.append(( 1, a, b, x, k, l, r))
        while(d):
            t,a,b,x,k,l,r = d.pop()
            if(t > 0): 
                self.eval(k)
                if(a <= l and r <= b):
                    self.lazy[k] = x
                    self.eval(k)
                elif(a < r and l < b):
                    d.append((-1, a, b, x, k*2 + 2, (l+r)//2, r))
                    d.append(( 1, a, b, x, k*2 + 2, (l+r)//2, r))
                    d.append((-1, a, b, x, k*2 + 1, l, (l+r)//2))
                    d.append(( 1, a, b, x, k*2 + 1, l, (l+r)//2))
            else:
                if(a <= l and r <= b): pass
                elif(a < r and l < b):
                    self.dat[k] = self.func(self.dat[k*2 + 1], self.dat[k*2 + 2])

    def update(self, a, b, x): # 半開区間 [a, b) の値を xに更新
        self.update_sub(a, b, x, 0, 0, self.num)

    def query_sub(self, a, b, k, l, r):
        d = deque()
        # d.append((-1, a, b, k, l, r))
        d.append(( 1, a, b, k, l, r))
        ret = self.ide_ele
        while(d):
            t,a,b,k,l,r = d.pop()
            if(t > 0):
                self.eval(k)
                if(r <= a or b <= l): ret = self.func(ret, self.ide_ele)
                elif(a <= l and r <= b): ret = self.func(ret, self.dat[k])
                else:
                    # d.append((-1, a, b, k*2 + 2, (l+r)//2, r))
                    d.append(( 1, a, b, k*2 + 2, (l+r)//2, r))
                    # d.append((-1, a, b, k*2 + 1, l, (l+r)//2))
                    d.append(( 1, a, b, k*2 + 1, l, (l+r)//2))
            else:
                pass
        return ret

    def query(self, a, b): # 半開区間 [a, b) のクエリ
        return self.query_sub(a, b, 0, 0, self.num)


# [sample_func] 最小値を求める
# def func(x, y):
#     return max(x,y)
# ide_ele = 0

# [ex. Tenkei 029]