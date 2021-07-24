class SegTree:
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
