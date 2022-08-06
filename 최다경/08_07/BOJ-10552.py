import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, c = MIS()
fa = []
ha = []
cnt = 0
for i in range(n):
    f, h = MIS()
    fa.append(f)
    ha.append(h)
  
changer = 0
visited = [False for _ in range(n)]

while(1):
    if c not in ha:
        print(cnt)
        exit(0)
    if c in ha:
        changer = ha.index(c)
        c = fa[changer]
        if visited[changer]:
            print(-1)
            exit(0)
        visited[changer] = True
    cnt += 1
