import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [list(input().rstrip().split()) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
flag = False
t = []
def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def find(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                t.append([i, j])
    return t

t = find(arr)
print(t)
def bfs():
    for pos in t:
        for dir in range(4):
            ny, nx = pos

            while in_range(ny, nx):
                if arr[ny][nx] == 'O':
                    break
                if arr[ny][nx] == 'S':
                    return False
                
                ny = ny + dy[dir]
                nx = nx + dx[dir]
    return True

def sol(cnt):
    global flag
    if cnt == 3:
        if bfs():
            flag = True
            return None
    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    sol(cnt + 1)
                    arr[i][j] = 'X'

sol(0)
if flag == False:
    print('NO')
else: print('YES')
            

