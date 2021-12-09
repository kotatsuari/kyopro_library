# 後ろが ok のパターン
def isOK(mid, key):
    ret = (a[mid] > key)
    return ret

def binary_search(key):
    ng = -1
    ok = len(a)
    while(abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if(isOK(mid, key)): ok = mid
        else: ng = mid
    return ok


# 前が ok のパターン
def isOK(mid, key):
    ret = (a[mid] < key)
    return ret

def binary_search(key):
    ng = len(a)
    ok = -1
    while(abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if(isOK(mid, key)): ok = mid
        else: ng = mid
    return ok


# 任意のリストから探索するパターン
def isOK(a, mid, key):
    ret = (a[mid] > key)
    return ret

def binary_search(a, key):
    ng = -1
    ok = len(a)
    while(abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if(isOK(a, mid, key)): ok = mid
        else: ng = mid
    return ok