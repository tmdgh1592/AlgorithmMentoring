#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(y, x, size):
    global res
    if y == r and x == c:
        print(res)
        return None
    
    if r < y + size and y <= r and c < x + size and x <= c:
        div = size // 2
        f(y, x, div)
        f(y, x + div, div)
        f(y + div, x, div)
        f(y + div, x + div, div)
    else:
        res += size * size

n, r, c = MIS()
res = 0
f(0, 0, (1 << n))