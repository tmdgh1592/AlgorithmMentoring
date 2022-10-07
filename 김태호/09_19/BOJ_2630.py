#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

arr = [list(MIS()) for _ in range(int(input()))]
res = [0, 0]

def f(y, x, size):
    here = arr[y][x]
    for i in range(size):
        for j in range(size):
            if arr[y + i][x + j] != here:
                size //= 2
                f(y, x, size)
                f(y + size, x, size)
                f(y, x + size, size)
                f(y + size, x + size, size)
                return
    res[arr[y][x]] += 1

f(0, 0, len(arr))
print(*res,sep='\n')
