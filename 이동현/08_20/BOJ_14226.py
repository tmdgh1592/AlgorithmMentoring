import sys
from collections import deque

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())

visited = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
visited[1][0] = 0

q = deque()
q.append((1, 0))

while q:
    node = q.popleft()
    cur_emoji, clip_board = node

    if cur_emoji == n:
        print( visited[cur_emoji][clip_board])
        exit()
    
    if visited[cur_emoji][cur_emoji] == -1:
        visited[cur_emoji][cur_emoji] = visited[cur_emoji][clip_board] + 1
        q.append((cur_emoji, cur_emoji))

    if (cur_emoji + clip_board <= n) and visited[cur_emoji + clip_board][clip_board] == -1:
        visited[cur_emoji + clip_board][clip_board] = visited[cur_emoji][clip_board] + 1
        q.append((cur_emoji + clip_board, clip_board))
    
    if (cur_emoji - 1 >= 0) and visited[cur_emoji - 1][clip_board] == -1:
        visited[cur_emoji - 1][clip_board] = visited[cur_emoji][clip_board] + 1
        q.append((cur_emoji - 1, clip_board))