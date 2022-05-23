# N과 M (8)
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    
    for i in range(num, N):       
        result.append(lst[i])
        func(i)
        result.pop()

func(0)
