# N과 M (1)
N, M = map(int, input().split())
result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(1, N + 1):
        if i in result:
            continue
        result.append(i)
        func(num + 1)
        result.pop()

func(0)
