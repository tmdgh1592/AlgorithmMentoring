# def f(arr):
#     if len(arr) == 3:
#         print(*arr)
#         return None
    
#     for i in range(1, 4):
#         if i in arr: continue;
        
#         arr.append(i)
#         f(arr)
#         arr.pop()
        
# f(list())


#m, n = map(int, input().split())
n, m = map(int, input().split())


def permutation(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return None
    
    for i in range(1, n+1):
        if i in arr: continue

        arr.append(i)
        permutation(arr, n, m)
        arr.pop()

permutation(list(), n, m)
