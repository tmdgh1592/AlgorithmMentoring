#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 16)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(idx):
    if cache[idx] != float('inf'):
        return cache[idx]
    
    remain = m - data[idx]
    
    for next_idx in range(idx + 1, n + 1):
        if remain < 0:
            break
        if next_idx == n:
            cache[idx] = 0
            break
        cache[idx] = min(remain * remain + f(next_idx), cache[idx])
        remain -= data[next_idx] + 1
    return cache[idx]

n, m = MIS()
data = [int(input()) for _ in range(n)]
cache = [float('inf') for _ in range(n)]
cache[-1] = 0
print(f(0))