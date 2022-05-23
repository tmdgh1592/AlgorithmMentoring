n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()

def permutation(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return None
    
    for i in list1:
        if i in arr: continue

        arr.append(i)
        permutation(arr, n, m)
        arr.pop()

permutation(list(), n, m)
#solved
