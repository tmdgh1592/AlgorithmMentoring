import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(MIS()))
arr.sort(key = lambda x: (x[1], x[0]))
# print(arr)

end = arr[0][1]
cnt = 1

for i  in range(1, n):
    if arr[i][0] >= end:
        end = arr[i][1]
        cnt += 1
print(cnt)