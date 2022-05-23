tmp = 0

n = int(input())
arr = [list(input()) for _ in range(n)]

def check_max_row(arr, row):
    tmp_cnt = 1
    max_cnt = 1

    for i in range(n - 1):
        if arr[row][i] == arr[row][i+1]:
            tmp_cnt += 1
            max_cnt = max(tmp_cnt, max_cnt)
        else:
            tmp_cnt = 1
    return max_cnt

def check_max_col(arr, col):
    
    tmp_cnt = 1
    max_cnt = 1

    for i in range(n - 1):
        if arr[i][col] == arr[i+1][col]:
            tmp_cnt += 1
            max_cnt = max(tmp_cnt, max_cnt)
        else:
            tmp_cnt = 1
    return max_cnt

def candy(arr, n):
    candy_max = 1
    for i in range(n):
        for j in range(n-1):
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            candy_max = max(check_max_col(arr, j), check_max_row(arr, i),check_max_col(arr, j+1), candy_max)
            print(arr)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    for i in range(n):
        for j in range(n-1):
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            candy_max = max(check_max_row(arr, j+1), check_max_row(arr, j),check_max_col(arr, i), candy_max)
            print(arr)
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

    print(candy_max)


candy(arr, n)

