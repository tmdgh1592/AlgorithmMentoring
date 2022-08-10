#-*- coding:utf-8 -*-
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MAX_INT = int(1e5)

n, k = MIS()
q = deque()
visited = [0 for _ in range(MAX_INT + 1)]
q.append((n, 0))
res = defaultdict(int)
data = [-1 for _ in range(int(1e5) + 1)]

def dfs(here):
    if here == -1: return
    dfs(data[here])
    print(here, end=' ')
    return 

while q:
    cur_node = q.popleft()
    
    cur_pos, cur_time = cur_node
    visited[cur_pos] = True
    
    if cur_pos == k:
        print(cur_time)
        dfs(cur_pos)
        break
    
    if cur_pos * 2 <= MAX_INT and not visited[cur_pos * 2]:
        if data[cur_pos * 2] == -1:
            data[cur_pos * 2] = cur_pos
        q.append((cur_pos * 2, cur_time + 1))
        
    if cur_pos + 1 <= MAX_INT and not visited[cur_pos + 1]:
        if data[cur_pos + 1] == -1:
            data[cur_pos + 1] = cur_pos
        q.append((cur_pos + 1, cur_time + 1))
    
    if cur_pos - 1 >= 0 and not visited[cur_pos - 1]:
        if data[cur_pos - 1] == -1:
            data[cur_pos - 1] = cur_pos
        q.append((cur_pos - 1, cur_time + 1))
