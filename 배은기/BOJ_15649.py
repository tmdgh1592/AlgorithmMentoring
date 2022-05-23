N, M = map(int, input().split())

def func(temp):
    if len(temp) == M:
        print(*temp)
        return None

    for here in range(1, N+1):
        if here not in temp:
            temp.append(here)
            func(temp)
            temp.pop()

func(list())
