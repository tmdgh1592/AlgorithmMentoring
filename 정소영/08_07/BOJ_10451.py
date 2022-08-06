#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(num):
    if visited[num]: return True

    visited[num] = True
    next = arr[num]
    if not visited[next]: 
        dfs(next)


t = int(input())

for _ in range(t):
    cnt = 0
    n = int(input())
    arr = [0] + list(MIS())
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)