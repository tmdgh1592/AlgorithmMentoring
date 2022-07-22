import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, s = MIS()
number = list(MIS())
res = 0

for i in range(1, (1 << n)):
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += number[j]
    if sum == s:
        res += 1
print(res)