nm = list(map(int,input().split()))
n = nm[0]
m = nm[1]
arr = []
def per(n, m, here):
    if m == 0:
        print(*arr, sep=" ")
        return None
    for there in range(here + 1, n):
        arr.append(there+1)
        per(n, m-1, there)
        arr.pop()
per(n, m, -1)