import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
lg = [input().rstrip().split()[0] for _ in range(n)]
c = Counter(lg)
lst = []
for key in c:
    if c[key] % 2 != 0:
        #print(key)
        lst.append(key)
lst = sorted(lst, reverse = True)

for i in range(len(lst)):
    print(lst[i])


