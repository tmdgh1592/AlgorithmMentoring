#-*- coding:utf-8 -*-
import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MAX_INT = int(1e5)

n, k = MIS()
q = deque()
visited = [0 for _ in range(MAX_INT + 1)]
q.append((n, 0))

while q:
    cur_node = q.popleft()
    
    cur_pos, cur_time = cur_node
    visited[cur_pos] = True
    
    if cur_pos == k:
        print(cur_time)
        break
    
    if cur_pos + 1 <= MAX_INT and not visited[cur_pos + 1]:
        q.append((cur_pos + 1, cur_time + 1))
    
    if cur_pos - 1 >= 0 and not visited[cur_pos - 1]:
        q.append((cur_pos - 1, cur_time + 1))
    
    if cur_pos * 2 <= MAX_INT and not visited[cur_pos * 2]:
        q.append((cur_pos * 2, cur_time + 1))
        
