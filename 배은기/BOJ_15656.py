N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

def func(temp):
    if len(temp) == M:
        print(*temp)
        return None

    for here in range(N):
            temp.append(L[here])
            func(temp)
            temp.pop()

func(list())
