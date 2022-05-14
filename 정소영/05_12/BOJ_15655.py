# N과 M (6)
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(num, N):
        if lst[i] not in result:
            result.append(lst[i])
            func(i + 1)
            result.pop()

func(0)
