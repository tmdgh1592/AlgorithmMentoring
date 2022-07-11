MAX_SIZE = 3000
arr =[[" "]*MAX_SIZE for _ in range(MAX_SIZE)]
n = int(input())

def baseStar(arr, x, y):
    for i in range(3):
        for j in range(3):
            if i == j and i == 1:
                continue
            arr[x+i][y+j] = "*"


def star(n, x, y):
    if n == 3:
        baseStar(arr, x, y)
        return None
    for i in range(3):
        for j in range(3):
            if i == j and i == 1:
                continue
            star(n//3, x+(n//3*i), y+(n//3*j))

def printStar(arr,n):
    star(n,0,0)
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end="")
        print()
printStar(arr,n)