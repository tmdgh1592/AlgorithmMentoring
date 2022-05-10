import copy
nm = list(map(int,input().split()))
num = list(map(int,input().split()))
n = nm[0]
m = nm[1]
num.sort()
arr = []
index = []
prev = -1
prevLen = -1

def per(n, m, here, prev, prevLen):
    if m == 0:
        print(*arr, sep=" ")
        return None
    for there in range(here + 1, n):
        if num[there] == prev and prevLen == len(arr) + 1 :
            continue
        arr.append(num[there])
        per(n, m-1, there, prev, prevLen)
        prevLen = len(arr)
        prev = arr.pop()
per(n, m, -1, prev, prevLen)