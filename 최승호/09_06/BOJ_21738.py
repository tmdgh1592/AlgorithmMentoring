import sys
sys.setrecursionlimit(int(1e9))

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


N, S, P = MIS()
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    node, dest = MIS()
    graph[node].append(dest)
    graph[dest].append(node)

visited = [False] * (N+1)
flag = False
counts = []

def dfs(num, node):
    global flag

    if visited[node] or flag:
        return
    if node == P:
        flag = True
        counts.append(num)
        return
    
    visited[node] = True
    
    for x in graph[node]:
        dfs(num+1, x)

for i in range(1, S+1):
    flag = False
    dfs(0, i)


# 가장 적게 깰 수 있는 지지대까지의 경로 2개의 길이
# 펭귄이 서 있는 얼음
# 을 제외한 값을 출력
print(N - sum(sorted(counts)[:2]) - 1)