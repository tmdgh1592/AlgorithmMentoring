import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
arr = [int(input()) for _ in range(n)]
res = 0

for i in range(n - 1, -1, -1):
    if arr[i] > k: continue
    res += k // arr[i]
    k %= arr[i]
print(res)
