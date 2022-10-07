import sys
input = sys.stdin.readline

n = int(input())
r = [int(input()) for _ in range(n)]
r = sorted(r)
m = 0
for i in range(n):
    m = max(r[n - i - 1] * (i + 1), m)
print(m)

