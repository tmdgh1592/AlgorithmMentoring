from collections import defaultdict
import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
visited = [False for _ in range(n)]
d = defaultdict(list)

def dfs(person, count):
    visited[person] = True
    if count == 4:
        print(1)
        exit()
    for i in d[person]:
        if visited[i]: continue
        dfs(i, count + 1)
        visited[i] = False

for i in range(m):
    a, b = MIS()
    d[a].append(b)
    d[b].append(a)

for i in range(n):
    dfs(i, 0)
    visited[i] = False

print(0)