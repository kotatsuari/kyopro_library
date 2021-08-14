# オイラーツアー
# 木を探索する順序を記録

# 初期化
junjo = []
IN = [-1]*n
OUT = [-1]*n
count = 0

# 再帰ver.
def euler_tour(v, p, G):
    junjo.append(v)
    global count
    if(IN[v] == -1): IN[v] = count
    OUT[v] = count 
    count += 1
    for to in G[v]:
        if(to == p): continue
        euler_tour(to, v, G)
        junjo.append(v)
        OUT[v] = count 
        count += 1