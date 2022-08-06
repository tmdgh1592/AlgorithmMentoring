#틀림
import sys
from collections import deque

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [2, -2, 2, -2, 1, 1, -1, -1]
dx = [1, -1, -1, 1, 2, -2, 2, -2]
visited =[]
q = deque(list())

def in_range(y, x):
    global len
    return (y >= 0 and y < len) and (x >= 0 and x < len)

for _ in range(int(input())):
    cnt = 0
    len = int(input())
    now = list(MIS())
    want = list(MIS())
    visited = [[0 for _ in range(len)] for _ in range(len)]
    
    q.append(now)
    a, b = now
    visited[a][b] = 1
    
    while q:
        tmp = q.popleft()
        y, x = tmp
        des_y, des_x = want
        if y == des_y and x == des_x:
            print("ans", visited[y][x] - 1)
            break
            
        for dir in range(8):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny, nx): continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])


            




