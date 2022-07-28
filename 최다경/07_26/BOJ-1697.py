import sys
from collections import deque

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
q = deque()
MAX = int(1e5) + 1
visited = [False for _ in range(MAX)]
q.append((n, 0)) # position, time

while(q):
    tmp = q.popleft()
    pos, t = tmp 
    visited[pos] = True

    if pos == m:
        print(t)
        break
    
    if (pos + 1) <= (MAX - 1) and not visited[pos + 1]:
        q.append((pos + 1, t + 1))

    if (pos - 1) >= 0 and not visited[pos - 1]:
        q.append((pos - 1, t + 1))

    if (pos * 2) <= (MAX - 1) and not visited[pos * 2]:
        q.append((pos * 2, t + 1))
