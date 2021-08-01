# 迷路問題用

# 再帰ver  pypyだとめっちゃ遅い
def maze(x, y, s, dis):
    for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx = x+dx; ny = y+dy
        if(not(0 <= nx < h) or not(0 <= ny < w)): continue
        if(s[nx][ny] == '#'): continue
        if(dis[nx][ny] <= dis[x][y]+1): continue
        dis[nx][ny] = dis[x][y] + 1
        maze(nx, ny, s, dis)


# 非再帰ver 使うならこっち
from collections import deque
def maze(sx, sy, s, dis):
    stack = deque()
    stack.append((-1, sx, sy))
    stack.append(( 1, sx, sy))
    while(stack):
        t,x,y = stack.pop()
        if(t == 1):
            for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx = x+dx; ny = y+dy
                if(not(0 <= nx < h) or not(0 <= ny < w)): continue
                if(s[nx][ny] == '#'): continue
                if(dis[nx][ny] <= dis[x][y]+1): continue
                dis[nx][ny] = dis[x][y] + 1
                stack.append((-1, nx, ny))
                stack.append(( 1, nx, ny))
        else: 
            pass


# [ex. ABC 151 D]