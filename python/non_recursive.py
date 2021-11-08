# 非再帰 dfs

from collections import deque

a = 0
used = [False]*n

def dfs3(s):
    global a
    stack = deque()
    stack.append((-1, s))
    stack.append((1, s))
    while(stack):
        (t,v) = stack.pop()
        if(t == 1): # 行きがけ
            if(used[v]): continue
            used[v] = True
            a += 1
            for to in G[v]:
                if(not used[to]): 
                    stack.append((-1, to))
                    stack.append((1, to))
        else:       # 帰りがけ
            pass
