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

for i in range(n): #선생님의 위치를 큐에 추가
    for j in range(n):
        if hall[i][j] == 'T':
            q.append((i, j))
# print(q)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def check(q_copy):
    i = 0
    while q_copy:
        cur_node = q_copy.popleft()
        i += 1
        y, x = cur_node
        # print("선생님 초기 위치: ", y, x, i)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            while in_range(ny, nx) and hall[ny][nx] != 'O':
                # print(ny,nx,hall[ny][nx])
                if hall[ny][nx] == 'S':
                    return False
                ny += dy[dir]
                nx += dx[dir]
    return True

def install_wall(cnt):
    if cnt == 3:
        if check(q.copy()):
            print('YES')
            exit()
        return None
    for i in range(n):
        for j in range(n):
            if hall[i][j] == 'X':
                hall[i][j] = 'O'
                install_wall(cnt + 1)
                hall[i][j] = 'X'



install_wall(0)
print('NO')