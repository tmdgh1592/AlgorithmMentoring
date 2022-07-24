import sys
sys.setrecursionlimit(1 << 14)
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = [[False for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]
count = 0

def in_range(y, x):
    global n
    return (x >= 0 and x < n) and (y >= 0 and y < n)

def dfs(person, count):
    visited[person] = True

    if count == 4: # 깊이가 4가 되면 1을 출력하고 종료
        print(1)
        exit()
    for i in range(n):  #인원 수만큼 반복
        if not visited[i]:
            if not arr[person][i]: continue # 친구 관계 형성하지 않으면 뛰어 넘음
            dfs(i, count + 1)
            visited[i] = False

for _ in range(m): #친구 관계 표시
    a, b = MIS()
    arr[a][b] = True
    arr[b][a] = True
    
for i in range(n):
            dfs(i, count)
            visited[i] = False
print(0)