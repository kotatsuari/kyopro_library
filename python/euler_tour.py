IN = [-1]*n
OUT = [-1]*n
count = 0
def euler_tour(v, p, G):
    global count
    if(IN[v] == -1): IN[v] = count
    OUT[v] = count 
    count += 1
    for to in G[v]:
        if(to == v): continue
        euler_tour(to, v, G)