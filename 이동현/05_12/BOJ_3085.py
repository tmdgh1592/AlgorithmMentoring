size = int(input())
arr = []
for _ in range(size):
    temp = list(map(str, input()))
    arr.append(temp)

def check(size, arr, switch):
    max = 1
    continuous = 1
    if switch == 0:
        for i in range(size):
            for j in range(size-1):
                if arr[i][j] == arr[i][j+1]:
                    continuous += 1
                    if continuous >= max:
                        max = continuous
                else:
                    continuous = 1
            continuous = 1
    else:
        for i in range(size):
            for j in range(size-1):
                if arr[j][i] == arr[j+1][i]:
                    continuous += 1
                    if continuous >= max:
                        max = continuous
                else:
                    continuous = 1
            continuous = 1
    return max

def getMax(size, arr):
    row = check(size, arr, 0)
    col = check(size, arr, 1)
    return max(row,col)

def startGame(size, arr):
    max = 0
    temp = 0
    for i in range(size):
        for j in range(size-1):
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = getMax(size, arr)
            if temp >= max:
                max = temp
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    for i in range(size):
        for j in range(size-1):
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            temp = getMax(size, arr)
            if temp >= max:
                max = temp
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
    return max

print(startGame(size,arr))
