# アフィン変換

import math
class affine_trans:
    def __init__(self): # 初期化
        pass
    
    def basic(self): # 基本形を返す
        ret = [[1,0,0],[0,1,0],[0,0,1]]
        return ret

    def product(self, A, B): # ret = A×B
        ret = [[0]*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                ret[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + A[i][2]*B[2][j]
        return ret

    def transformation(self, A, u): # 行列 A をベクトル u にかける
        ret = [0,0]
        ret[0] = A[0][0]*u[0] + A[0][1]*u[1] + A[0][2]
        ret[1] = A[1][0]*u[0] + A[1][1]*u[1] + A[1][2]
        return ret    

    def rotation(self, A, t): # t度回転
        t = math.radians(t)
        rotate = [[math.cos(t),-math.sin(t),0],
                    [math.sin(t),math.cos(t),0],
                    [0,0,1]]
        return self.product(rotate, A)
    
    def int_rotation(self, A, t): # t度回転(90度回転のみ対応)
        t = math.radians(t)
        rotate = [[int(math.cos(t)),int(-math.sin(t)),0],
                    [int(math.sin(t)),int(math.cos(t)),0],
                    [0,0,1]]
        return self.product(rotate, A)

    def x_reflection(self, A, p): # x=p で反転
        refrect = [[-1,0,2*p],[0,1,0],[0,0,1]]
        return self.product(refrect, A)

    def y_refrection(self, A, q): # y=q で反転
        refrect = [[1,0,0],[0,-1,2*q],[0,0,1]]
        return self.product(refrect, A)

# [ex. ABC 189 E]