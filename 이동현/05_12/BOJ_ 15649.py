nm = list(map(int,input().split()))
n = nm[0]
m = nm[1]
arr = []
def per(n, m):
    if m == 0:
        print(*arr, sep=" ")
        return None
    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        per(n, m-1)
        arr.pop()
per(n, m)