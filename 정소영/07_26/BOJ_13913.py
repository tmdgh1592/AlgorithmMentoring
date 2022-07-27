#-*- coding:utf-8 -*-
from collections import defaultdict, deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

MAX = int(1e5)

n, k = MIS()
q = deque()
visited = [False for _ in range(MAX + 1)]
q.append((n, 0))

time = 0
path = defaultdict(list)

def move(path):
    global time
    temp = k

    res = []
    res.append(k)
    for i in range(time - 1, 0, -1):
        if temp / 2 in path[i]:
            res.append(int(temp / 2))
            temp = int(temp / 2)
        elif temp - 1 in path[i]:
            res.append(temp - 1)
            temp = temp - 1
        elif temp + 1 in path[i]:
            res.append(temp + 1)
            temp = temp + 1

    res.append(n)
    res.reverse()
    return res
    
while q:
    cur_node = q.popleft()

    cur_pos, cur_time = cur_node
    visited[cur_pos] = True

    path[cur_time].append(cur_pos)

    if cur_pos == k:
        time = cur_time
        break

    if cur_pos + 1 <= MAX and not visited[cur_pos + 1]:
        q.append((cur_pos + 1, cur_time + 1))

    if cur_pos - 1 >= 0 and not visited[cur_pos - 1]:
        q.append((cur_pos - 1, cur_time + 1))

    if cur_pos * 2 <= MAX and not visited[cur_pos * 2]:
        q.append((cur_pos * 2, cur_time + 1))

print(time)
print(*move(path))
#틀렸습니다