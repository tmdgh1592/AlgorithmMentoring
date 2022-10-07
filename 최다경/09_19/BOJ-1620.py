import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
pocket_dict = defaultdict()
for i in range(n):
    pocket_dict[i] = input().rstrip()
pocket_rdict = {v:k for k,v in pocket_dict.items()}
res = [input().rstrip() for _ in range(m)]

for key in res:
    if key.isalpha():
        print(pocket_rdict[key] + 1)
    else:
        print(pocket_dict[int(key) - 1])
