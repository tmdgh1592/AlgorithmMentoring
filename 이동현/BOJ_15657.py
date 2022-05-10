nm = list(map(int,input().split()))
num = list(map(int,input().split()))
n = nm[0]
m = nm[1]
num.sort()
arr = []

def per(n, m):
    if m == 0:
        print(*arr, sep=" ")
        return None
    for i in range(0, n):
        if(len(arr) != 0 and num[i] < arr[-1]):
            continue
        arr.append(num[i])
        per(n, m-1)
        arr.pop()
per(n, m)