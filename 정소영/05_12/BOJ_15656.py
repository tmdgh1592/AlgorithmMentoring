# N과 M (7)
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(N):
        result.append(lst[i])
        func(num + 1)
        result.pop()

func(0)
