#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 16)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(x):
    if x >= n: return float('inf')
    if x == n - 1:
        return 0
    if cache[x] != float('inf'):
        return cache[x]
    
    for jump_size in range(1, data[x] + 1):
        cache[x] = min(f(x + jump_size) + 1, cache[x])
    return cache[x]
n = int(input())
cache = [float('inf') for _ in range(n)]
data = list(MIS())
res = f(0)
print(res if res != float('inf') else -1)