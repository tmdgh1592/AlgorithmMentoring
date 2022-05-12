N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

def func(temp):
    if len(temp) == M:
        print(*temp)
        return None

    for here in L:
        if here not in temp:
            temp.append(here)
            func(temp)
            temp.pop()

func(list())
