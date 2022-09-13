import sys

input = sys.stdin.readline
MIS = lambda: input().rstrip()

n, m = map(int, (input().rstrip().split()))
arr = [list(MIS()) for _ in range(n)]
def is_empty(a, b):
    if a == '.':
        return b
    else: return a

for i in range(n):
    for j in range(m // 2):
        tmp = is_empty(arr[i][j], arr[i][m-j-1])
        if arr[i][j] == '.':
            arr[i][j] = tmp
        else: arr[i][m-j-1] = tmp

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()