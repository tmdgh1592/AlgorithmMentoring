import sys
from collections import defaultdict

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0

def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def dfs(pos):
    global cnt
    for i in g[pos]:
        if visited[i]:
            cnt += 1
            exit(0)
        if not visited[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False

for _ in range(int(input())):
    n = int(input())
    arr = list(MIS())
    cnt = 0
    # data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited = [False for _ in range(n)]
    g = defaultdict(list)
    for i in range(n):
        # print(i)
        # data[i + 1][arr[i]] = 1
        # data[arr[i]][i + 1] = 1\
        u, v = i + 1, arr[i]
        g[u].append(v)
        g[v].append(u)
    for j in range(n):
        visited[j] = True
        dfs(j)
        visited[j] = False
    print(cnt)

    
                
