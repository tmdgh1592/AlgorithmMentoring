import sys
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
MAX_INT = int(1e5)
q = deque()
q.append((n, 0))
# min = float('inf')
def in_range(n):
    return n >= 0 and n <= MAX_INT
visited = [False for _ in range(MAX_INT + 1)]
#잘못된 풀이
# def bfs(pos, time):
#     global min
#     pos = q.popleft()
#     visited[pos] = True
#     if pos == k:
#         if min > time:
#             min = time

#     if not visited[pos + 1] and in_range(pos + 1):
#         q.append(pos + 1)
#         bfs(pos + 1, time + 1)

#     if not visited[pos - 1] and in_range(pos - 1):
#         q.append(pos - 1)
#         bfs(pos - 1, time + 1)
        
#     if not visited[pos * 2] and in_range(pos * 2):
#         q.append(pos * 2)
#         bfs(pos * 2, time + 1)

# bfs(n, 0)

while q:
    cur_node = q.popleft()
    cur_pos, time = cur_node
    visited[cur_pos] = True

    if cur_pos == k:
        print(time)
        exit()
    if in_range(cur_pos + 1) and not visited[cur_pos + 1]:
        q.append((cur_pos + 1, time + 1))
    if in_range(cur_pos - 1) and not visited[cur_pos - 1]:
        q.append((cur_pos - 1, time + 1))
    if in_range(cur_pos * 2) and not visited[cur_pos * 2]:
        q.append((cur_pos * 2, time + 1))