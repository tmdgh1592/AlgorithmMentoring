import copy
nm = list(map(int,input().split()))
num = list(map(int,input().split()))
n = nm[0]
m = nm[1]
num.sort()
arr = []
prev = -1
prevLen = -1

def per(n, m, prev, prevLen):
    if len(arr) == m:
        print(*arr, sep=" ")
        return None
    for i in range(0, n):
        if num[i] == prev and prevLen == len(arr) + 1 :
            continue
        arr.append(num[i]) 
        per(n, m, prev, prevLen)
        prevLen = len(arr)
        prev = arr.pop()
per(n, m, prev, prevLen)