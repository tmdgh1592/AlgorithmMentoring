#뭐가 틀렸을까...
import sys
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
hall = list()
q = deque()
q_copy = deque()

for _ in range(n):
    hall.append(input().rstrip().split())
print(hall)

for i in range(n): #선생님의 위치를 큐에 추가
    for j in range(n):
        if hall[i][j] == 'T':
            q.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

wall = list()

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def check():
    global q_copy
    cnt = 0
    while q_copy:
        cur_node = q_copy.popleft()
        y, x = cur_node
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            while in_range(ny, nx) and hall[i][j] != 'O':
                if hall[ny][nx] == 'S':
                    cnt += 1
                    return cnt
                ny += dy[dir]
                nx += dx[dir]
    return cnt

def install_wall():
    if len(wall) == 3:
        init()
        cnt = check()
        print(cnt)
        if cnt == 0:
            print(wall)
            print('YES')
            exit()
        return None
    for i in range(n):
        for j in range(n):
            if hall[i][j] == 'X':
                hall[i][j] = 'O'
                wall.append((i, j))
                install_wall()
                wall.pop()
                hall[i][j] = 'X'

def init():
    global q, q_copy
    q_copy = q
    return None
install_wall()
print('NO')