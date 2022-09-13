#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, r, c = MIS()

cnt = 0

def z(x, y, n):

    global cnt

    if x == r and y == c:
        print(cnt)
        exit(0)

    mid = n // 2

    if (x <= r < x + n and y <= c < y + n):
    
        z(x, y, mid)
        z(x, y + mid, mid)
        z(x + mid, y, mid)
        z(x + mid, y + mid, mid)

    else:
        
        cnt += n * n

print(z(0,0,pow(2,n)))