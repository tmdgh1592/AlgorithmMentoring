from stringprep import in_table_c11
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
arr = [0 for _ in range(100)]
if n == 0:
    print(0)
    exit(0)
seat = list(MIS())
cnt = 0

for i in range(n):
    arr[seat[i] - 1] += 1
for i in range(100):
    if arr[i] != 1 and arr[i] != 0:
        cnt += arr[i] - 1
print(cnt)
#런타임에러??


