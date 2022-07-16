#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = [input().rstrip() for _ in range(n)]
res = -1

for i in range(1 << (n * m)):
    total = 0
    
    for j in range(n):
        cur = 0
        
        for k in range(m):
            pos = j * m + k
            
            if i & (1 << pos):
                total += cur
                cur = 0
            
            else:
                cur = cur * 10 + int(data[j][k])
        total += cur

    for j in range(m):
        cur = 0
        
        for k in range(n):
            pos = k * m + j
            
            if not (i & (1 << pos)):
                total += cur
                cur = 0
            
            else:
                cur = cur * 10 + int(data[k][j])
        total += cur
    res = max(total, res)

print(res)
