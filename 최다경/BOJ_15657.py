n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()
def check(arr):
    check_arr = arr.copy()
    check_arr.sort()
    cor = 0
    for i in range(len(arr)):
        if arr[i] != check_arr[i]: cor = 1
    if cor == 0: return 1
    else: return -1

def permutation(arr: list, n, m):
    if len(arr) > 0 and check(arr) == -1: return None
    if len(arr) == m:
        print(*arr)
        return None

    for i in list1:
        arr.append(i)
        #print('arr: ', arr)
        permutation(arr, n, m)
        arr.pop()

permutation(list(), n, m)

