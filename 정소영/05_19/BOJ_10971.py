n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
res = 987654321

def least_cost(start, y, sum, cnt):
    global res

    if cnt == n and start == y:
        if res > sum:
            res = sum
            return None

    for x in range(n):
        if arr[y][x] == 0: 
            continue

        if res >= sum and arr[x][y] > 0: 
            if not visited[y]: 
                visited[y] = True
                sum += arr[y][x]
                least_cost(start, x, sum, cnt + 1)
                visited[y] = False
                sum -= arr[y][x]

for y in range(n):
    least_cost(y, y, 0, 0)

print(res)
