import code
import sys
from collections import deque
import heapq
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
sea = list()# 전체 지도
baby_position = tuple() #아기 상어 위치
baby_size = 2 #아기 상어 크기
eat_cnt = 0 #아기 상어가 먹은 물고기 수
res = 0

for i in range(n):
    temp = list(MIS())
    if 9 in temp:
        baby_position = (0,i,temp.index(9),0) #거리, 아기 상어 위치, 시간(이동거리)
        temp2 = temp.index(9)
        temp[temp2] = 0
    sea.append(temp)

q = deque()
q.append(baby_position)

#위쪽 우선, 왼쪽 우선 탬색을 위해 다음과 같이 정의
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def in_range(y, x): return (0 <= y) and (y < n) and (0 <= x) and(x < n)


def bfs():
    global baby_size, eat_cnt, res
    visited = [[False] * n for _ in range(n)]
    while q:
        #큐의 각 노드에는 y,x 좌표와 현재 그 좌표까지 걸린 시간이 들어있음
        cur_node = heapq.heappop(q)
        y, x , time= cur_node
        visited[y][x] = True
        #만약 아기 상어 크기보다 작으면 먹기
        if (sea[y][x] != 0) and (sea[y][x] < baby_size): 
            sea[y][x] = 0
            eat_cnt += 1
            res = max(time,res)
            #먹었으니까 visited 배열을 모두 초기화 해준다.
            visited = [[False] * n for _ in range(n)]
            #큐 역시 비워주고 새로 시작
            q.clear()
            visited[y][x] = True
            #아기 상어 크기랑 먹은 물고기 수 같으면 크기 증가
            if baby_size == eat_cnt: 
                baby_size += 1
                #먹은 횟수는 0으로 초기화
                eat_cnt = 0
        
        for dir in range(4):
            ny = y + dy[dir] #위쪽 먼저
            nx = x + dx[dir] #왼쪽 먼저
            if not in_range(ny, nx): continue
            if visited[ny][nx]: continue
            if sea[ny][nx] > baby_size: continue
            q.append((ny, nx, time + 1))

bfs()
print(res)