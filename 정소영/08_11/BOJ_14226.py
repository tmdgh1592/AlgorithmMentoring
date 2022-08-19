#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

s = int(input())

q = deque()
q.append((1,0,0)) # screen, clip, time

visited = [[False for _ in range(1001)] for _ in range(1001)]
visited[1][0] = True

def in_range(s, c):
    return (c < 1001 and c > 0) and (s < 1001 and s > 0)

while q:
    screen, clip, time = q.popleft()
    
    if screen == s: 
        print(time)
        break

    for i in range(3):
        if i == 0:
            ns = screen
            nc = screen
            

        elif i == 1:
            ns = screen + clip
            nc = clip

        else:
            ns = screen - 1
            nc = clip

        if not in_range(ns,nc): continue
        if not visited[ns][nc]:
            visited[ns][nc] = True
            q.append((ns, nc, time + 1))
