#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return y >= 0 and y < r and x >= 0 and x < c

r, c = MIS()
data = [list(MIS()) for _ in range(r)]
res = 0

block = [
    [[0,1], [0,2], [0,3]],
    [[1,0], [2,0], [3,0]],
    [[1,0], [1,1], [1,2]],
    [[0,1], [1,0], [2,0]],
    [[0,1], [0,2], [1,2]],
    [[1,0], [2,0], [2,-1]],
    [[0,1], [0,2], [-1,2]],
    [[1,0], [2,0], [2,1]],
    [[0,1], [0,2], [1,0]],
    [[0,1], [1,1], [2,1]],
    [[0,1], [1,0], [1,1]],
    [[0,1], [-1,1], [-1,2]],
    [[1,0], [1,1], [2,1]],
    [[0,1], [1,1], [1,2]],
    [[1,0], [1,-1], [2,-1]],
    [[0,1], [0,2], [-1,1]],
    [[0,1], [0,2], [1,1]],
    [[1,0], [2,0], [1,1]],
    [[1,0], [2,0], [1,-1]],
]


for i in range(r):
    for j in range(c):
        for k in range(19):
            flag = True
            cur_sum = data[i][j]
            for l in range(3):
                y = i + block[k][l][0]
                x = j + block[k][l][1]
                
                if in_range(y, x):
                    cur_sum += data[y][x]
                else:
                    flag = False
                    break
            if flag:
                res = max(cur_sum, res)

print(res)


# ---------------------------------------------------------------------
#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return y >= 0 and y < r and x >= 0 and x < c

def f(depth, y, x):
    if depth == 4:
        return 0
    
    ret = 0
    
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        visited[ny][nx] = True
        ret = max(f(depth + 1, ny, nx) + data[y][x], ret)
        visited[ny][nx] = False
    return ret

def g(y, x):
    ret = 0
    for rotation in range(4):
        res = data[y][x]
        
        for dir in range(3):
            ny = y + dy[(rotation + dir) % 4]
            nx = x + dx[(rotation + dir) % 4]
            
            if not in_range(ny, nx):
                res = 0
                break
            res += data[ny][nx]
        ret = max(res, ret)
    return ret

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

r, c = MIS()
data = [list(MIS()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
res = 0

for i in range(r):
    for j in range(c):
        visited[i][j] = True
        res = max(f(0, i, j), res)
        visited[i][j] = False
        res = max(g(i, j), res)

print(res)