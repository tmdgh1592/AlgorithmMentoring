import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(pos, depth):
    if depth == 4:
        print(1)
        exit(0)
    
    for i in g[pos]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

n, m = MIS()
g = defaultdict(list)
depth = 0
visited = [False for _ in range(n)]

for i in range(m): #defaultdict(<class 'list'>, {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]})
    u, v = MIS()
    g[u].append(v)
    g[v].append(u)

for j in range(m):
    visited[j] = True
    dfs(j, 0)
    visited[j] = False

print(0)



