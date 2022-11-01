import sys, copy
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n, m = MIS()
ice = [list(MIS()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
near = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
pos = deque()
pos2 = deque()
last = 0
cnt = 0

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)

def side(y, x): #해당 블럭 상하좌우에 얼음이 몇개 있는지 체크
    s_cnt = 0
    for dir in range(4):
        if ice[y + dy[dir]][x + dx[dir]] <= 0: s_cnt += 1
    return s_cnt

def brk(): #얼음 깨는 함수
    for i in range(n):
        for j in range(m):
            tmp = ice[i][j] - near[i][j]
            if tmp < 0: ice[i][j] = 0
            else: ice[i][j] = tmp

def empty():#얼음이 모두 깨졌는지 확인
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                return False
    return True
    




#pos 배열은 매인으로 사용할 얼음 위치 큐, pos2는 1년 단위로 다음 년도까지 녹지 않을 얼음 저장 큐
# while pos:
#     tmp = pos.popleft()
#     #print(tmp)
#     y, x = tmp
#     visited[y][x] = True
#     near[y][x] = side(y, x)#near배열에 현재 얼음이 옆에 몇개의 얼음과 맞붙어있는지 담음
#     if near[y][x] < ice[y][x]: pos2.append((y, x))#녹지않으면 내년까지 남아있는 얼음에 추가
#     if tmp == last:#pos가 마지막 얼음이면
#         brk()#얼음 깨줌 
#         print(ice, end='\n')
#         if not empty(): cnt += 1
#         else: break     
#         if not pos2: break

        
#         visited = [[False for _ in range(m)] for _ in range(n)]
#         near = [[0 for _ in range(m)] for _ in range(n)]#초기화
        
#         last = pos2[-1]
#         pos = copy.deepcopy(pos2)
#         pos2 = deque()#pos를 pos2로 초기화 하고 pos2 비워줌
    

#     for dir in range(4):#4방향 탐색
#         ny = y + dy[dir]
#         nx = x + dx[dir]
#         if not in_range(ny, nx): continue
#         if ice[ny][nx] <= 0: continue
#         if visited[ny][nx]: continue
#         visited[ny][nx] = True
# if not flag and cnt == 0: print(1)
# else: print(cnt)
#deque([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)])
#deque([(3, 4), (1, 3), (2, 4), (3, 1), (3, 2)])

#얼음 깎고, bfs - 2개 이하면 다시 깎음

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while pos:
        y, x = pos.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny, nx): continue
            if ice[ny][nx] == 0: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = True
            print(ny, nx)
            q.append((ny, nx))


for i in range(n):
    for j in range(m):
        if ice[i][j] != 0:
            pos.append((i, j))
res = 0
i = 0
while 1:
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and ice[i][j]:
                bfs(i, j)
                res += 1
                print(res)





