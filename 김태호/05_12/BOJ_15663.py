#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS() 
to_pick = sorted(list(MIS()))
visited = [False for _ in range(n)]

def recursion(lst):
    if len(lst) == m:
        print(*lst)
        return None
    
    last_element = -1
    
    for i in range(n):
        if visited[i]: continue;
        if last_element == to_pick[i]: continue;
        last_element = to_pick[i]
        visited[i] = True
        lst.append(to_pick[i])
        recursion(lst)
        visited[i] = False
        lst.pop()


recursion(list())
