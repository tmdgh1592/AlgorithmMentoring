import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
dic = defaultdict(set)
n, m = MIS()
res = float('inf')

for _ in range(m):
    a, b = MIS()
    dic[a].add(b)
    dic[b].add(a)
print(dic)
for i in range(1, n + 1):
    for j in dic[i]:
        for k in dic[j]:
            if i in dic[k]:
                print(len(dic[i]), len(dic[j]), len(dic[k]), "ijk:", i, j, k)
                res = min(len(dic[i]) + len(dic[j]) + len(dic[k]) - 6, res )

if res != float('inf'):
    print(res)
else:
    print(-1)