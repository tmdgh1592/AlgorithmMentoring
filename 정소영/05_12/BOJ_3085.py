n = int(input())

arr = [input().rstrip() for _ in range(n)]
arr = [list(map(ord, arr[row])) for row in range(n)]

res = 1

dy = [1, 0]
dx = [0, 1]

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def is_end(y, x):
    return (y == n - 1) and (x == n - 1)

def check():
    global res

    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if arr[i][j] == arr[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            if res < cnt :
                res = cnt

        cnt = 1
        
        for j in range(n - 1):
            if arr[j][i] == arr[j + 1][i]:
                cnt += 1
            else:
                cnt = 1

            if res < cnt :
                res = cnt

def recursion(y, x):
    if is_end(y, x):
        return None
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny, nx): 
            continue

        arr[ny][nx], arr[y][x] = arr[y][x], arr[ny][nx]
        check()
        arr[ny][nx], arr[y][x] = arr[y][x], arr[ny][nx]
        recursion(ny, nx)

recursion(0, 0)
print(res)