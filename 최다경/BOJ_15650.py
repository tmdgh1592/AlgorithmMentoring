n, m = map(int, input().split())
entry = 1 
def permutation(arr, n, m, entry):
    tmp = 0
    if len(arr) == m:
        print(*arr)
        return None
    
    for i in range(entry, n+1):

        arr.append(i)
        entry += 1
        permutation(arr, n, m, entry)
        post = arr.pop()

permutation(list(), n, m, entry)
#solved
