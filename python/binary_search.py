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