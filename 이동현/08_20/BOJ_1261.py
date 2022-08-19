import sys
from collections import deque

sys.setrecursionlimit(1 << 14)

MIS = lambda: map(int, input())

m, n  = map(int, input().rstrip().split())
miro = []
for _ in range(n):
    miro.append(list(MIS()))

visited = [[False for _ in range(m)] for _ in range(n)] #방문 기록

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return (x >= 0 and x < m) and (y >= 0 and y < n)

q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    cur_node = q.popleft()
    y, x = cur_node # c는 벽을 부순 횟수 (crash)

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue

        if miro[ny][nx] <= 0:
            q.appendleft((ny, nx))
            visited[ny][nx] = True
            miro[ny][nx] -= abs(miro[y][x])

        else:
            q.append((ny, nx))
            visited[ny][nx] = True
            miro[ny][nx] = miro[ny][nx] + (abs(miro[y][x]))


print(min(abs(miro[n - 2][m - 1]), abs(miro[n - 1][m - 2])))


