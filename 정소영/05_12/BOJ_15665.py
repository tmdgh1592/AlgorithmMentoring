# N과 M (11)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []

def func(num) :
    if len(result) == M :
        print(*result)
        return None
    re_num = 0
    for i in range(N):
        if  re_num != lst[i] :
            result.append(lst[i])
            re_num = lst[i]
            func(num + 1)
            result.pop()

func(0)
 