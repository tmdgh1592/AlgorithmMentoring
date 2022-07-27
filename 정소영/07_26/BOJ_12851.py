#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

MAX = int(1e5)
n, k = MIS()
q = deque()
visited = [False for _ in range(MAX + 1)]
q.append((n, 0))

cnt = 0
time = 0

while q:
    cur_node = q.popleft()

    cur_pos, cur_time = cur_node
    visited[cur_pos] = True

    if cur_pos == k:
        if time == 0:
            time = cur_time
            cnt += 1
        elif time == cur_time:
            cnt += 1
        else:
            break

    if cur_pos + 1 <= MAX and not visited[cur_pos + 1]:
        q.append((cur_pos + 1, cur_time + 1))

    if cur_pos - 1 >= 0 and not visited[cur_pos - 1]:
        q.append((cur_pos - 1, cur_time + 1))

    if cur_pos * 2 <= MAX and not visited[cur_pos * 2]:
        q.append((cur_pos * 2, cur_time + 1))

print(time, cnt, sep='\n')
