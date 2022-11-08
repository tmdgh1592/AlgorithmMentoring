import sys

MIS = lambda: map(int, input().rstrip().split())
n, m = MIS()

lstA = [list(map(int, list(input()))) for _ in range(n)]
lstB = [list(map(int, list(input()))) for _ in range(n)]

def rvs(i, j):
    print(i, j)
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            if lstA[k][l] == 0:
                lstA[k][l] = 1
            else:
                lstA[k][l] = 0

cnt = 0
if(n < 3 or m < 3):
    if lstA != lstB:
        cnt = -1
else:
    for r in range(n - 2):
        for c in range(m - 2):
            if lstA[r][c] != lstB[r][c]:
                cnt += 1
                rvs(r, c)

if lstA != lstB:
    cnt = -1
print(cnt)
