# N과 M (3)
N, M = map(int, input().split())
result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(num, N + 1):
        result.append(i)
        func(num + 1)
        result.pop()

func(1)
