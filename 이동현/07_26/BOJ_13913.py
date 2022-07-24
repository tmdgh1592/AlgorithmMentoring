import sys
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
MAX_INT = int(1e5)
q = deque()
q.append((n, 0))
arr = [-1 for _ in range(MAX_INT + 1)]

def in_range(n):
    return n >= 0 and n <= MAX_INT
visited = [False for _ in range(MAX_INT + 1)]


while q:
    cur_node = q.popleft()
    cur_pos, time = cur_node

    visited[cur_pos] = True
    
    if cur_pos == k:
        print(time)
        pos_q = deque()
        for _ in range(time + 1):
            pos_q.appendleft(cur_pos)
            cur_pos = arr[cur_pos]
        print(*pos_q)
        exit()

    if in_range(cur_pos + 1) and not visited[cur_pos + 1]:
        q.append((cur_pos + 1, time + 1))
        arr[cur_pos + 1] = cur_pos

    if in_range(cur_pos - 1) and not visited[cur_pos - 1]:
        q.append((cur_pos - 1, time + 1))
        arr[cur_pos - 1] = cur_pos

    if in_range(cur_pos * 2) and not visited[cur_pos * 2]:
        q.append((cur_pos * 2, time + 1))
        arr[cur_pos * 2] = cur_pos