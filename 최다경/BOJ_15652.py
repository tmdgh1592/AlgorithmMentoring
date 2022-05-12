n, m = map(int, input().split())
entry = 1 
post = 1

def check(arr):
    check_arr = arr.copy()
    check_arr.sort()
    cor = 0
    for i in range(len(arr)):
        if arr[i] != check_arr[i]: cor = 1
    if cor == 0: return 1
    else: return -1

def permutation(arr, n, m, post):
    tmp = 0
    if len(arr) > 0 and check(arr) == -1: return None
    if len(arr) == m:
        print(*arr)
        return None
    
    for i in range(post, n+1):
        if tmp > i: continue

        arr.append(i)
        post = arr[0]
        permutation(arr, n, m, post)
        tmp = arr.pop()

permutation(list(), n, m, post)
#solved
