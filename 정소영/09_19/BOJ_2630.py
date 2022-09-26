#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [list(MIS()) for _ in range(n)]

blue = 0
white = 0

size = n
def func(y, x, size):

    global blue, white
    
    mid = size // 2

    cur = arr[y][x]
    for ny in range(y, y + size):
        for nx in range(x, x + size):
            if cur != arr[ny][nx]:
                func(y, x, mid)
                func(y, x + mid, mid)
                func(y + mid, x, mid)
                func(y + mid, x + mid, mid)
                return
    if cur == 0: white += 1
    else: blue += 1

func(0,0,size)
print(white, blue, sep='\n')