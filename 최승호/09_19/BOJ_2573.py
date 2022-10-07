#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = []
ice_list = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    row = list(MIS())
    for j in range(m):
        if row[j] != 0: ice_list.append((i, j)) # 빙하 위치 체크
    arr.append(row)


def melt(ice, x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < n and 0 <= ny < m) and arr[nx][ny] == 0 and not ice[nx][ny]:
            arr[x][y] -= 1
            if arr[x][y] == 0: return True

    return False

def check(visited, x, y):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]:
            check(visited, nx, ny)
    return 1

def is_seperate():
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for x, y in ice_list:
        if not visited[x][y] and arr[x][y]:
            cnt += check(visited, x, y)
            if cnt > 1: return True
                
    return False

def is_all_melted():
    return len(ice_tmp_list) == len(ice_list)


ice_tmp_list = []
time = 0
while True:
    time += 1
    ice_visit = [[False] * m for _ in range(n)]

    for idx, (x, y) in enumerate(ice_list):
        if x != 0 and y != 0:
            ice_visit[x][y] = True
            if melt(ice_visit, x, y):
                ice_list[idx] = (0, 0)
                ice_tmp_list.append(0)
    
    if is_all_melted(): # 빙산이 다 녹아버린 경우
        print(0)
        break
    if is_seperate(): # 빙산이 분리된 경우
        print(time)
        break