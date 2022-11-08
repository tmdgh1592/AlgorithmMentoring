#재귀로 풀려다 변경
import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m= MIS()
relation = [[False] * n for _ in range(n)]
d = defaultdict(int)
cnt = int(1e9)

for i in range(m):
    a, b = MIS()
    relation[a - 1][b - 1] = True
    relation[b - 1][a - 1] = True
    d[a - 1] += 1
    d[b - 1] += 1

flag = False

for i in range(n):
    for j in range(i + 1, n):
        if not relation[i][j]: continue
        for k in range(j + 1, n):
            if not relation[i][k] or not relation[j][k]: continue
            flag = True
            temp = d[i] + d[j] + d[k] - 6
            if cnt > temp: cnt = temp

if flag: print(cnt)
else: print(-1)