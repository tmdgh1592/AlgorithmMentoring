import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
arr = sorted(list(MIS()))

for i in range(1, n):
    arr[i] += arr[i - 1]
print(sum(arr))