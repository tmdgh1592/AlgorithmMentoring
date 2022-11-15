import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
d = defaultdict()
arr = []
n, m = MIS()
for _ in range(n):
    s, p = input().rstrip().split()
    d[s] = p
for _ in range(m):
    arr.append(input().rstrip())

for site in arr:
    pw = d[site].rstrip()
    print(d[site])

    