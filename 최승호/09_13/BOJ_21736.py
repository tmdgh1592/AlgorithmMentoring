from collections import deque
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0

def bfs(x, y):
    global cnt
    q = deque([(x,y)])

    while q:
        nowX, nowY = q.popleft()

        if not (0 <= nowX < n and 0 <= nowY < m):
            continue
        if visited[nowX][nowY]:
            continue
        if arr[nowX][nowY] == 'X':
            continue

        visited[nowX][nowY] = True

        if arr[nowX][nowY] == 'P':
            cnt += 1
        q.append((nowX-1, nowY))
        q.append((nowX+1, nowY))
        q.append((nowX, nowY-1))
        q.append((nowX, nowY+1))

iX, iY = 0, 0

flag = False

for i in range(n):

    if flag:

        break

    for j in range(m):
         if arr[i][j] == 'I':
             iX, iY = i, j
             flag=True
             break

bfs(iX, iY)

if cnt == 0:
    print('TT')
else:
    print(cnt)