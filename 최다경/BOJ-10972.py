n = int(input())
arr = list(map(int, input().split()))
idx1 = 0
idx2 = 0
ma = 0
tmp_arr = []
sort_point = 0
def np(arr, n):
    global idx1, idx2, ma
    tmp = 0
    i = len(arr) - 1
    k = len(arr) - 1
    if len(arr) == 1:
        print(-1)
        return None
    while(i > 0 and arr[i] <= arr[i - 1]):
        tmp_arr.append(arr[i])
        i -= 1
    tmp_arr.append(arr[i])

    while(k > 0):
        if arr[k] > arr[k - 1]:
            idx1 = k - 1
            break
        k -= 1
        if k == 0:
            print(-1)
            return None
            
    for i in range(0, len(tmp_arr)):
        if arr[idx1] < tmp_arr[i]: 
            tmp = tmp_arr[i]
            break

    idx2 = arr.index(tmp)
    sort_point = arr.index(max(tmp_arr))
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    arr[sort_point:] = arr[len(arr) - 1: sort_point - 1: -1]
    #arr[sort_point:] = sorted(arr[sort_point:])
    print(*arr)
    return None
np(arr, n)
