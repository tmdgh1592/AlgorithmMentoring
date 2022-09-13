from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(int(1e9))

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

graph = []
teachers_xy = deque()
dx, dy = [-1,1,0,0], [0,0,-1,1]
answer = False

n = int(input())

for i in range(n):
    teacher = list(input().rstrip().split())
    graph.append(teacher)
    for j in range(n):
        if teacher[j] == 'T':
            teachers_xy.append((i, j))


def search():
    q = deepcopy(teachers_xy)

    while q:
        x, y = q.popleft()

        for i in range(4):
            tx, ty = x, y

            while True:
                nx, ny = tx+dx[i], ty+dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    tx, ty = nx, ny

                    if graph[nx][ny] == 'S':
                        return False      
                    if graph[nx][ny] == 'O':
                        break
                else:
                    break

    return True


def dfs(cnt):
    global answer

    if answer:
        return
    if cnt == 3:
        if search():
            answer = True
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(cnt+1)
                graph[i][j] = 'X'


dfs(0)
print('YES') if answer else print('NO')