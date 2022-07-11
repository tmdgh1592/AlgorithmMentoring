MIS = lambda: map(int, input().rstrip().split())
n = int(input())
cost = [list(MIS()) for _ in range(n)]
min_w = float('inf')
visited = []
def travel(weight):
    temp = 0
    global min_w
    if len(visited) == n:
        if cost[visited[-1]][visited[0]] != 0:
            weight += cost[visited[-1]][visited[0]]
            min_w = min(min_w, weight)
        return None
    for i in range(n):
        if i in visited : #도시를 방문한 경우 건너뜀
            continue
        if visited and cost[visited[-1]][i] == 0: #다음 도시까지 길이 없으면 건너뜀
            continue
        if visited and weight + cost[visited[-1]][i] > min_w: #다음 도시까지 가중치를 더했는데 최솟값보다 크면 건너뜀
            continue
        if visited:
            temp = cost[visited[-1]][i]
        visited.append(i)
        travel(weight + temp)
        visited.pop()
travel(0)
print(min_w)
