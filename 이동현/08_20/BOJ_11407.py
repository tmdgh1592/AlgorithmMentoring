import sys
sys.setrecursionlimit(1 << 14)

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n, k = MIS()
temp = k
temp2 = 0
value = [int(input()) for _ in range(n)]
res = 0
for i in range(n - 1, -1, -1):
    if temp >= value[i]:
        temp2 = temp // value[i]
        temp -= temp2 * value[i]
        res += temp2
print(res)