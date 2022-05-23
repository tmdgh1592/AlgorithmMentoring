t = int(input())
arr = [int(input()) for _ in range(t)]

cnt = 0

def f(n, goal):
    global cnt

    if n == goal:
        cnt += 1
        return None

    if n > goal:
        return None

    for i in range(1,4):
        f(n + i, goal)


for i in range(t):
    f(0, arr[i])
    print(cnt)
    cnt = 0 