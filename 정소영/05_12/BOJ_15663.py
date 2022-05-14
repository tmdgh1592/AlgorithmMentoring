# N과 M (9)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

visited = [False for _ in range(N)]
result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None

    re_num = 0
    for i in range(N):
        if visited[i]: 
            continue
        if re_num == lst[i]:
            continue
        visited[i] = True
        result.append(lst[i])
        re_num = lst[i]
        func(num + 1)
        visited[i] = False
        result.pop()

func(0)


