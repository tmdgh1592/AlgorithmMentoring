N, M = map(int, input().split())

def func(temp,start):
    if len(temp) == M:
        print(*temp)
        return None

    for here in range(start, N+1):
            temp.append(here)
            func(temp,here)
            temp.pop()

func(list(),1)
