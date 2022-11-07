import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = [list(MIS()) for _ in range(n)]

def in_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < m

block = [
    [[0, 1], [0, 2], [0, 3]],
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [1, 0], [1, 1]],
    [[1, 0], [2, 0], [2, 1]],
    [[0, 1], [0, 2], [1, 0]],
    [[0, 1], [1, 1], [1, 2]],
    [[0, 1], [1, 1], [2, 1]], 
    [[0, 1], [0, 2], [-1, 2]], 
    [[0, 1], [0, 2], [1, 2]], 
    [[1, 0], [2, 0], [0, 1]], 
    [[1, 0], [2, 0], [2, -1]],
    [[1, 0], [1, 1], [2, 1]],
    [[1, 0], [1, -1], [2, -1]],
    [[1, 0], [1, 1], [1, 2]], 
    [[0, 1], [1, 0], [1, -1]],
    [[1, 0], [1, -1], [1, 1]],
    [[1, 0], [1, 1], [2, 0]],
    [[0, 1], [0, 2], [1, 1]],
    [[1, 0], [2, 0], [1, -1]],
]

sum = 0
res = 0
for i in range(n):
    for j in range(m):
        for k in range(19):
            sum = data[i][j]
            flag = True
            for l in range(3):
                y = i + block[k][l][0]
                x = j + block[k][l][1]
                if in_range(y, x):
                    sum += data[y][x]
                else:
                    flag = False
                    break
            if flag:
                res = max(sum, res)

               

print(res)