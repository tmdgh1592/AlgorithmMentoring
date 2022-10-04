#-*- coding:utf-8 -*-
import heapq
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return y >= 0 and y < len(data) and x >= 0 and x < len(data)

def get_init_pos():
    n = len(data)
    for i in range(n):
        for j in range(n):
            if data[i][j] == 9:
                data[i][j] = 0
                return (0, i, j)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
data = [list(MIS()) for _ in range(int(input()))]
visited = [[False for _ in range(len(data))] for _ in range(len(data))]
size = 2
ate = 0
res = 0

q = list()
q.append(get_init_pos())

while q:
    d, y, x = heapq.heappop(q)
    
    if 0 < data[y][x] < size:
        data[y][x] = 0
        ate += 1
        if ate == size:
            size += 1
            ate = 0
        
        res += d
        d = 0
        
        visited = [[False for _ in range(len(data))] for _ in range(len(data))]
        q = list()
    
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if size < data[ny][nx]: continue
        heapq.heappush(q, (d + 1, ny, nx))
        visited[ny][nx] = True
print(res)