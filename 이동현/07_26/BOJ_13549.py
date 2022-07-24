import sys
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
MAX_INT = int(1e5)
q = deque()
q.append((n, 0))

def in_range(n):
    return n >= 0 and n <= MAX_INT
visited = [False for _ in range(MAX_INT + 1)]

while q:
    cur_node = q.popleft()
    cur_pos, time = cur_node
    visited[cur_pos] = True

    if cur_pos == k:
        print(time)
        exit()

    if in_range(cur_pos * 2) and not visited[cur_pos * 2]: #왼쪽에 추가해서 우선 순위를 높임
        q.appendleft((cur_pos * 2, time))
    if in_range(cur_pos + 1) and not visited[cur_pos + 1]:
        q.append((cur_pos + 1, time + 1))
    if in_range(cur_pos - 1) and not visited[cur_pos - 1]:
        q.append((cur_pos - 1, time + 1))