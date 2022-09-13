#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] != '.':
            arr[i][m-j-1] = arr[i][j]
            
for i in range(n):
    for j in range(m):
        print(arr[i][j],end='')
    print()