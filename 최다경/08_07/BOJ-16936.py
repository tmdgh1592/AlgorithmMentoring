from operator import truediv
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())
per = []
visited = [False for _ in range(n)]

def f():
    if len(per) == n:
        print(*per)
        exit(0)

    for i in range(n):
        if visited[i]: continue

        if arr[i] == per[-1] * 2:
            per.append(arr[i])
            visited[i] = True
            f()
            per.pop()
            visited[i] = False

        if arr[i] == per[-1] // 3 and per[-1] % 3 == 0:
            per.append(arr[i])
            visited[i] = True
            f()
            per.pop()
            visited[i] = False

for i in range(n):
    per.append(arr[i])
    visited[i] = True
    f()
    per.pop()
    visited[i] = False