#-*- coding:utf-8 -*-
import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MAX_INT = int(5e5)

n, k = MIS()
q = deque()
visited = [[0 for _ in range(2)] for _ in range(MAX_INT + 1)]
q.append((n, 0))
visited[n][0] = True

while q:
    cur_pos, cur_time = q.popleft()    
    
    if k + cur_time * (cur_time + 1) // 2 > MAX_INT:
        print(-1)
        break
    
    if visited[k + cur_time * (cur_time + 1) // 2][cur_time % 2]:
        print(cur_time)
        break
    
    if cur_pos + 1 <= MAX_INT and not visited[cur_pos + 1][(cur_time + 1) % 2]:
        q.append((cur_pos + 1, cur_time + 1))
        visited[cur_pos + 1][(cur_time + 1) % 2] = cur_time + 1
    
    if cur_pos - 1 >= 0 and not visited[cur_pos - 1][(cur_time + 1) % 2]:
        q.append((cur_pos - 1, cur_time + 1))
        visited[cur_pos - 1][(cur_time + 1) % 2] = cur_time + 1
    
    if cur_pos * 2 <= MAX_INT and not visited[cur_pos * 2][(cur_time + 1) % 2]:
        q.append((cur_pos * 2, cur_time + 1))
        visited[cur_pos * 2][(cur_time + 1) % 2] = cur_time + 1
        
