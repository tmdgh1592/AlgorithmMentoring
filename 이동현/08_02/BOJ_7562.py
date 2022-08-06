import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

case_loop = int(input())

dy = [-2, -2, -1, 1, 2, 2, 1, -1]
dx = [-1, 1, 2, 2, 1, -1, -2, -2]

def in_range(y, x):
    global i
    return (x >= 0 and x < i) and (y >= 0 and y < i)

for _ in range(case_loop):
    q = deque()
    i = int(input())
    srt_x, srt_y = MIS()
    dest_x, dest_y = MIS()
    chess = [[0 for _ in range(i)] for _ in range(i)]
    q.append((srt_y, srt_x))
    chess[srt_y][srt_x] = 1
    while q:
        cur_node = q.popleft()
        y, x = cur_node
        if x == dest_x and y == dest_y:
            print(chess[y][x] -1)
            break
        for dir in range(8):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny, nx): continue
            if chess[ny][nx] == 0:
                chess[ny][nx] = chess[y][x] + 1
                q.append((ny, nx))