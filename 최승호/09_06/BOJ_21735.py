import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

N, M = MIS()
arr = [0] + list(MIS())
answer = 0

def dfs(idx, size, time):
    global answer

    # 시간 초과시 return : Backtracking
    if time > M: return

    answer = max(answer, size)

    if idx <= N-1:
        dfs(idx+1, size+arr[idx+1], time+1)
    if idx <= N-2:
        dfs(idx+2, size//2+arr[idx+2], time+1)

# 눈덩이 시작크기 : 1
dfs(0, 1, 0)
print(answer)