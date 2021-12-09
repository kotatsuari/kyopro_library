# Binary Indexed Tree
# リストに要素を加算が O(logN) でできる
# リストの区間和を O(logN) で取得できる

class BIT():    # 一点加算BIT ver
    def __init__(self, n):      # nは要素数
        self.n = n+1            # indexは1~nなので、長さをn+1にする
        self.bit = [0]*self.n   
        
    def add(self, i, x):        # i の要素に x を加算
        idx = i
        while(idx < self.n):
            # ここを変更で、加算以外にも使える
            self.bit[idx] += x

            idx += (idx & -idx) # 次のindexへ
        
    def sum(self, i):           # 1~i までの要素の和を出力
        idx = i; SUM = 0
        while(idx > 0):
            SUM += self.bit[idx]
            idx -= (idx & -idx) # 次のindexへ
        return SUM
    
    def query(self, l, r):      # 半開区間 [l, r) の和を出力
        return (self.sum(r-1) - self.sum(l-1))


class BIT_RAQ():    # 区間加算BIT ver
    def __init__(self, n):      # nは要素数
        self.n = n+1            # indexは1~nなので、長さをn+1にする
        self.bit = [[0]*self.n for i in range(2)]   

    def add_sub(self, p, i, x): # i の要素に x を加算
        idx = i
        while(idx < self.n):
            # ここを変更で、加算以外にも使える
            self.bit[p][idx] += x

            idx += (idx & -idx) # 次のindexへ
        
    def add(self, l, r, x):     # 半開区間 [l, r)に加算、iに値を入れたい時は [i, i+1)
        self.add_sub(0, l, -x * (l - 1))
        self.add_sub(0, r, x * (r - 1))
        self.add_sub(1, l, x)
        self.add_sub(1, r, -x)

    def sum_sub(self, p, i):    # bit[p] の 1~i までの要素の和を出力
        idx = i; SUM = 0
        while(idx > 0):
            SUM += self.bit[p][idx]
            idx -= (idx & -idx) # 次のindexへ
        return SUM
    
    def sum(self, i):           # 1~i までの要素の和を出力
        return self.sum_sub(0, i) + self.sum_sub(1, i) * i

    def query(self, l, r):      # 半開区間 [l, r) の和を出力、iの要素が欲しいときは [i, i+1)
        return (self.sum(r-1) - self.sum(l-1))


# 使い方例

# n = int(input())    
# BIT = BIT_RAQ(n)
#
# q = int(input())
# for i in range(q):
#     i,x = map(int, input().split())
#     BIT.add(i, i+3,x)
#
# for i in range(n+1):
#     print(i, BIT.sum(i))
#
# print(BIT.query(2, 5))

# ex. ABC153.F