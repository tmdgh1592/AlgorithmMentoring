import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()

web = defaultdict(str)
want = list()
for i in range(n):
    temp = list(input().rstrip().split())
    web[temp[0]] = temp[1]

for i in range(m):
    want.append(input().rstrip().split())

for i in want:
    print(web[i[0]])
