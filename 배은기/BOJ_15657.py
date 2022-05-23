N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

def func(temp, start):
    if len(temp) == M:
        print(*temp)
        return None

    for here in range(start, N):
            temp.append(L[here])
            func(temp, here)
            temp.pop()

func(list(), 0)
#haha
