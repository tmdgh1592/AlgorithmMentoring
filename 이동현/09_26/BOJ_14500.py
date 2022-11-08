import code
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
#dfs로 4번 진행하고 최댓값 찾는다.
#ㅗ모양을 확인한다. 이전 과정의 결과 값과 비교하여 최댓값 찾는다.

n, m = MIS()
paper = list()
for i in range(n):
    paper.append(list(MIS()))

max_val = 0
visited =[[False]* m for _ in range(n)]

dy= [-1, 1, 0, 0]
dx= [0, 0, -1, 1]

def in_range(y, x): return (0 <= y) and (y < n) and (0 <= x) and (x < m)

def ou_shape(y, x):
    if m == 1 or n == 1: return 0
    #모서리에 있는 경우
    if (y == 0 or y == n - 1) and (x == 0 or x == m - 1): return 0
    #위쪽 끝, 아래 끝에 있는 경우
    if (y == 0 or y == n - 1):
        if y == 0:
            return paper[y][x] + paper[y + 1][x] + paper[y][x - 1] + paper[y][x + 1]
        else:
            return paper[y][x] + paper[y - 1][x] + paper[y][x - 1] + paper[y][x + 1]
    #왼쪽, 오른쪽 끝에 있는 경우
    if (x == 0 or x == m - 1):
        if x == 0:
            return paper[y][x] + paper[y - 1][x] + paper[y + 1][x] + paper[y][x + 1]
        else:
            return paper[y][x] + paper[y - 1][x] + paper[y + 1][x] + paper[y][x - 1]
    sibza = paper[y][x] + paper[y - 1][x] + paper[y + 1][x] + paper[y][x - 1] + paper[y][x + 1]
    min_val = min(paper[y - 1][x], paper[y + 1][x], paper[y][x - 1], paper[y][x + 1])
    return sibza - min_val

app = []

def dfs(y, x, cnt, s):
    global max_val
    if cnt == 4:
        if max_val < s: max_val =s
        # print(app, s)
        return None
    
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        visited[ny][nx] = True
        app.append((ny,nx))
        dfs(ny, nx, cnt + 1, s + paper[ny][nx])
        app.pop()
        visited[ny][nx] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        app.append((i,j))
        dfs(i, j, 1, paper[i][j])
        app.pop()
        visited[i][j] = False
        # print("max_val:", max_val)
        # print("ou: ",ou_shape(i, j))
        max_val = max(max_val, ou_shape(i, j))
print(max_val)