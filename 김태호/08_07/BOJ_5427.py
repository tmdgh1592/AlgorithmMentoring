#-*- coding:utf-8 -*-
import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global w, h
    return (y >= 0 and y < h) and (x >= 0 and x < w)

def init_pos():
    for i in range(h):
        for j in range(w):
            if data[i][j] == '@':
                sang_q.append((i, j, 0))
                visited_sang[i][j] = True
            if data[i][j] == '*':
                fire_q.append((i, j))
                visited_fire[i][j] = True


def burn():
    for _ in range(len(fire_q)) :
        y, x = fire_q.popleft()
        for dir in range(len(dy)):
            ny = y + dy[dir]
            nx = x + dx[dir]
            
            if not in_range(ny, nx): continue
            if visited_fire[ny][nx]: continue
            if data[ny][nx] != '#':
                data[ny][nx] = '*'
                visited_fire[ny][nx] = True
                fire_q.append((ny, nx))

def escape():
    for _ in range(len(sang_q)):
        y, x, t = sang_q.popleft()
        for dir in range(len(dy)):
            ny = y + dy[dir]
            nx = x + dx[dir]
            
            if not in_range(ny, nx):
                return t + 1
            if visited_sang[ny][nx]: continue
            if data[ny][nx] == '.':
                data[ny][nx] = '@'
                visited_fire[ny][nx] = True
                sang_q.append((ny, nx, t + 1))
    return -1


for _ in range(int(input())):
    w, h = MIS()
    data = [list(input().rstrip()) for _ in range(h)]
    
    visited_sang = [[False for _ in range(w)] for _ in range(h)]
    visited_fire = [[False for _ in range(w)] for _ in range(h)]
    
    sang_q = deque()
    fire_q = deque()
    
    init_pos()

    while sang_q or fire_q:
        burn()
        res = escape()
        if res != -1:
            break
        
    print(res if res != -1 else 'IMPOSSIBLE')

