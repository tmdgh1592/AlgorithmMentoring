import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
paint = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if paint[i][j] != '.':
            paint[i][m-j-1] = paint[i][j]

for i in range(n):
    print(*paint[i], sep='')