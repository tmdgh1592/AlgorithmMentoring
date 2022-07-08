#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def f(y, x):
    global n
    
    if y == n - 1 and x == n - 1:
        return 1

    if not in_range(y, x):
        return 0
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    jump_size = board[y][x]
    dp[y][x] = f(y + jump_size, x) or f(y, x + jump_size)
    return dp[y][x]

for _ in range(int(input())):
    n = int(input())
    board = [list(MIS()) for _ in range(n)]
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    print('YES' if f(0, 0) else 'NO')
