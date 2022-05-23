n, m = map(int, input().split())
list_1 = list(map(int, input().split()))
list_1.sort()

tmp = 0


def permutation(arr, n, m):
    global tmp
    if len(arr) == m:
        print(*arr)
        return None
    
    for i in list_1:
        if i in arr: continue
        if tmp == i: continue
        if len(arr) > 0 and arr[-1] > i: continue
        arr.append(i)
        permutation(arr, n, m)
        tmp = arr.pop()

permutation(list(), n, m)
#solved






