nm = list(map(int,input().split()))
num = list(map(int,input().split()))
n = nm[0]
m = nm[1]
num.sort()
arr = []

def per(n, m, here):
    if m == 0:
        print(*arr, sep=" ")
        return None
    for there in range(here + 1, n):
        arr.append(num[there])
        per(n, m-1, there)
        arr.pop()
per(n, m, -1)