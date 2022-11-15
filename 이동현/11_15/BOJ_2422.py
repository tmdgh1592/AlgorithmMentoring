from cgitb import reset
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
ice = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    temp1, temp2 = MIS()
    ice[temp1][temp2] = 1
    ice[temp2][temp1] = 1

res = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if ice[i][j] or ice[j][k] or ice[i][k]: continue
            res += 1

print(res)