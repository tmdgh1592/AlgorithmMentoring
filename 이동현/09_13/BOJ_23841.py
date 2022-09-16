import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()

d = list()

for _ in range(n):
    d.append(list(input().rstrip()))

for i in range(n):
    for j in range(m // 2):
        if d[i][j] != '.':
            d[i][-j - 1] = d[i][j]
        elif d[i][-j - 1] != '.':
            d[i][j] = d[i][-j - 1]
        else:
            continue
for i in d:
    print(''.join(i))