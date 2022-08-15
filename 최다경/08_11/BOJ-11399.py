import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())

arr = sorted(arr)
tmp = arr[0]
res = arr[0]
print(arr)
for i in range(1, n):
    tmp += arr[i]
    res += tmp
    print(tmp, res)
print(res)
