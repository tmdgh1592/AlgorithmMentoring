MAXYEAR = 100000
arr = list(map(int,input().split()))
def getYear(arr):
    
    for i in range(1,MAXYEAR):
        temp = arr
        if arr[0] == 15:
            arr[0] = 0
        if arr[1] == 28:
            arr[1] = 0
        if arr[2] == 19:
            arr[2] = 0
        if i % 15 == arr[0] and i % 28 == arr[1] and i % 19 == arr[2]:
            return i
        arr = temp
print(getYear(arr))
