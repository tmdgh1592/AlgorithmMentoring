# 왜 틀린지 모르겠습니다..
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

arr = []
res = 0
fs = -1

for _ in range(int(input())):
    arr.append(list(MIS()))

arr.sort(key = lambda x:x[1])

for i in range(len(arr)):
    s = arr[i][0]
    e = arr[i][1]
    if s > fs:
        res += 1
        fs = e

print(res)
