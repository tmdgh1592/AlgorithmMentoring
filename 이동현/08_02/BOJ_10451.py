import sys
sys.setrecursionlimit(1 << 14)

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
loop_cnt = int(input())

def dfs(x):
    visited[x] = True
    nx = case[x]
    if visited[nx]: return None
    dfs(nx)

for _ in range(loop_cnt):
    res = 0
    n = int(input())
    case = list(MIS())
    case.insert(0, 0)
    visited = [False for _ in range(n + 1)]

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            res += 1
    print(res)