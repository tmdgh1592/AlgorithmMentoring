# N과 M (4)
N, M = map(int, input().split())
result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(num, N + 1):
        result.append(i)
        func(i)
        result.pop()

func(1)
