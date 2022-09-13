#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def is_possible():
    for teacher in teachers:
        y, x = teacher
        for dir in range(len(dy)):
            ny, nx = y, x
            while True:
                ny += dy[dir]
                nx += dx[dir]
                if not in_range(ny, nx): break
                if data[ny][nx] == 'S':
                    return False
                if data[ny][nx] == 'O':
                    break
    return True

def f(cnt):
    global res
    if cnt == 3:
        if is_possible():
            res = 'YES'
        return None

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                f(cnt + 1)
                data[i][j] = 'X'
    return None

n = int(input())
data = [input().rstrip().split() for _ in range(n)]
teachers = list()
res = "NO"
for i in range(n):
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i, j))
f(0)
print(res)