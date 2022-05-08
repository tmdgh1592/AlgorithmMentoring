#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
board = [input().rstrip() for _ in range(n)]
board = [list(map(ord, board[row])) for row in range(n)]
res = 1

dy = [1, 0]
dx = [0, 1]

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def is_end(y, x):
    return (y == n - 1) and (x == n - 1)

def check():
    global res

    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                cnt +=1
            else:
                cnt = 1
            if cnt > res:
                res = cnt
        
        cnt = 1
        
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                cnt +=1
            else:
                cnt = 1
            if cnt > res:
                res = cnt
        

# def recursion(y, x):
#     if is_end(y, x):
#         return None
    
#     for dir in range(len(dy)):
#         ny = y + dy[dir]
#         nx = x + dx[dir]
        
#         if not in_range(ny, nx):
#             continue
        
#         board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
#         check()
#         board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
#         recursion(ny, nx)

def for_loop():
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                check()
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                
            if i + 1 < n:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                check()
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

# recursion(0, 0)
for_loop()
print(res)
