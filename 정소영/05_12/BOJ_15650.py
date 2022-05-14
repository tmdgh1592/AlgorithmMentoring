# N과 M (2)
N, M = map(int, input().split())
result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(num, N + 1):
        if i in result:
            continue
        result.append(i)
        func(i + 1)
        result.pop()

func(1)
