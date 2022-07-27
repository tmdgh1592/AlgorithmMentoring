#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

from collections import deque

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]

def in_range(y,x):
    global h,w
    return ((y >= 0 and y < h) and (x >= 0 and x < w))

def bfs(node):
    q = deque()
    q.append(node)
    
    while q:
        cur_node = q.popleft()

        for dir in range(8):
            ny = cur_node[0] + dy[dir]
            nx = cur_node[1] + dx[dir]

            if not in_range(ny, nx): continue
            if not arr[ny][nx]: continue
            arr[ny][nx] = 0
            q.append([ny, nx])
            
sys.setrecursionlimit(10**6)
def dfs(y,x) :

    for dir in range(8):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny,nx): continue
        if not arr[ny][nx]: continue
        arr[ny][nx] = 0
        dfs(ny,nx)

while True:
    w,h = MIS()
    
    if w == 0 and h == 0:
        break

    arr = [list(MIS()) for _ in range(h)]
    res = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                #bfs([i,j])
                dfs(i,j)
                res += 1
    print(res)
