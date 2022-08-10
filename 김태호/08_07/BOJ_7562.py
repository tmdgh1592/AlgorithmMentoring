#-*- coding:utf-8 -*-
import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    global l
    return (y >= 0 and y < l) and (x >= 0 and x < l)

dy = [2, 2, -1, 1, -2, -2, -1, 1]
dx = [-1, 1, 2, 2, -1, 1, -2, -2]

for _ in range(int(input())):
    l = int(input())
    cur_y, cur_x = MIS()
    target_y, target_x = MIS()
    visited = [[False for _ in range(l)] for _ in range(l)]
    q = deque()
    
    q.append((cur_y, cur_x, 0))
    visited[cur_y][cur_x] = True
    
    while q:
        y, x, movement = q.popleft()
        if (y, x) == (target_y, target_x):
            print(movement)
        
        for dir in range(len(dy)):
            ny = y + dy[dir]
            nx = x + dx[dir]
            
            if not in_range(ny, nx): continue
            if visited[ny][nx]: continue
            visited[ny][nx] = True
            q.append((ny, nx, movement + 1))
            
        