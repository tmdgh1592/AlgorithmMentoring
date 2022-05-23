
SIZE = 2500
box_size = 3
arr = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
x, y = 0, 0


def base_star(y,x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                arr[y + i][x + j] = '*'

def rf(y,x,box_size):
    if box_size == 3:
        base_star(y,x)
        return None
    next_box = box_size // 3

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                rf(y + i * next_box, x + j * next_box,next_box)

n = int(input())
rf(y, x, n)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()
