#-*- coding:utf-8 -*-
import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
cache = [[-1 for _ in range(1001)] for _ in range(1001)]
q = deque()
q.append((1, 0))
cache[1][0] = 0

while q:
    s, c = q.popleft()
    
    if cache[s][s] == -1:
        cache[s][s] = cache[s][c] + 1
        q.append((s, s))
    
    if s + c <= n and cache[s + c][c] == -1:
        cache[s + c][c] = cache[s][c] + 1
        q.append((s + c, c))
        
    if s - 1 >= 0 and cache[s - 1][c] == -1:
        cache[s - 1][c] = cache[s][c] + 1
        q.append((s - 1, c))
        
res = float('inf')

for i in range(n + 1):
    if cache[n][i] == -1: continue
    res = min(cache[n][i], res)
print(res)