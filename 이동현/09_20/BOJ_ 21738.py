import sys
from collections import deque, defaultdict
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, s, p = MIS()

d = defaultdict(list)

for _ in range(n-1):
    a, b = MIS()
    d[a].append(b)
    d[b].append(a)



def bfs(start, target):
    visited = defaultdict(list)
    q = deque()
    visited[start] = True
    q.append((start, 0))
    
    while q:
        cur_node = q.popleft()
        pos, cnt = cur_node
        if pos == target:
            return cnt
        for i in range(len(d[pos])):
            if visited[d[pos][i]]: continue
            visited[d[pos][i]] = True
            q.append((d[pos][i], cnt + 1))

rst = list()

for i in range(s):
    rst.append(bfs(i + 1,p))
rst = sorted(rst)

shortest = rst[0]+rst[1]
print(n - shortest - 1)
