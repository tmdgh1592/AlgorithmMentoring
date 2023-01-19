#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 16)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(days):
    if days > n:
        return -float('inf')

    if days == n:
        return 0

    if cache[days] != -1:
        return cache[days]
    
    cache[days] = 0
    cache[days] = max(f(days + 1), f(days + data[days][0]) + data[days][1])

    return cache[days]

n = int(input())
data = [list(MIS()) for _ in range(n)]
cache = [-1 for _ in range(n)]
print(f(0))