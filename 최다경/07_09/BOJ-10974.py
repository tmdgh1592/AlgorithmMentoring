n = int(input())
leng = n
def per(arr, n):
    if len(arr) == n:
        print(*arr)
        return None

    for i in range(1, n+1):
        if i in arr: continue

        arr.append(i)
        per(arr, n)
        arr.pop()

per(list(), n)
