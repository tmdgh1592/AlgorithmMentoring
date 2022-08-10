#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs():
    if len(res) == n:
        print(*res)
        exit(0)
    
    for i in range(n):
        if visited[i]: continue
        
        if data[i] == res[-1] * 2:
            res.append(data[i])
            visited[i] = True
            dfs()
            res.pop()
            visited[i] = False
            
        if data[i] == res[-1] // 3 and res[-1] % 3 == 0:
            res.append(data[i])
            visited[i] = True
            dfs()
            res.pop()
            visited[i] = False

n = int(input())
data = list(MIS())
visited = [False for _ in range(n)]
res = []

for i in range(n):
    res.append(data[i])
    visited[i] = True
    dfs()
    res.pop()
    visited[i] = False