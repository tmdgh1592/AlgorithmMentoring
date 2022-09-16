import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n, m = MIS()
arr = list(MIS())
arr.insert(0, 0)
ans = 0
print(arr)
def dfs(idx, s, t):
    global ans
    if t > m:
        return None
    if t <= m:
        ans = max(ans, s)
    if idx <= (n - 1):
        dfs(idx + 1, s + arr[idx + 1], t + 1)
    if idx <= (n - 2):
        dfs(idx + 2, s // 2 + arr[idx + 2], t + 1)
    
ans = -1
dfs(0, 1, 0)
print(ans)