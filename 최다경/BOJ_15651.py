n, m = map(int, input().split())

def permutation(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return None
    
    for i in range(1, n+1):
        arr.append(i)
        permutation(arr, n, m)
        arr.pop()

permutation(list(), n, m)

