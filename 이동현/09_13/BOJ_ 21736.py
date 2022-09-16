

#무슨 포켓몬스터냐 학교에서 상하좌우로만 이동하게

import sys
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
campus = list()

for i in range(n):
    campus.append(input().rstrip())
    if 'I' in campus[i]:
        temp = (i,campus[i].index("I"))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return (0<= y and y < n) and (0 <= x and x < m)

q = deque()
q.append(temp)

visited = [[False] * m for _ in range(n)]
cnt = 0

while q:
    cur_node = q.popleft()
    y, x = cur_node
    if campus[y][x] == 'P':
        cnt += 1

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx] : continue
        if campus[ny][nx] == 'X' : continue
        visited[ny][nx] = True
        q.append((ny, nx))
if cnt == 0:
    print('TT')
else:
    print(cnt)