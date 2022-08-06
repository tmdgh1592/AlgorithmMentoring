import sys
from collections import deque
import copy

MIS = lambda: map(int, input())

n, m = map(int, input().split())
data = [list(MIS()) for _ in range(n)]
arr = copy.deepcopy(data)
q = deque(list())
q.append([0, 0])
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)

def bfs(q, arr):
    global n, m
    while q:
        tmp = q.popleft()
        y, x = tmp
        step = arr[y][x]
        if y == n - 1 and x == m - 1:
            return arr[y][x]
        
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny, nx): continue
            if arr[ny][nx] != 0: continue
            arr[ny][nx] = step + 1
            q.append([ny, nx])

    return -1
res = []
tmp = 0
for i in range(n):
    for j in range(m):
        q.append([0, 0])
        arr = copy.deepcopy(data)
        if arr[i][j] == 1:
            arr[i][j] = 0
            tmp = bfs(q, arr)
            if tmp > 0: res.append(tmp)
if not res: 
    print(-1)
    exit(0)
print(min(res) + 1)
            
   
            


    