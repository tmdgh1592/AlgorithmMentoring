import sys
sys.setrecursionlimit(int(1e6))

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
star = [['*'] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def draw_star(x, y, interval):
    if x >= n or y >= n or visited[x][y]:
        return


    draw_empty(x, y, x+interval, y+interval)
    draw_star(x + 3*interval, y, interval)
    draw_star(x, y + 3*interval, interval)
    draw_star(3*x, 3*y, 3*interval)


def draw_empty(x, y, end_x, end_y):
    star[x][y] = ' '
    visited[x][y] = True
    
    if x + 1 < end_x and x + 1 < n:
        if not visited[x+1][y]:
            draw_empty(x+1, y, end_x, end_y)
    
    if y + 1 < end_y and y + 1 < n:
        if not visited[x][y+1]:
            draw_empty(x, y+1, end_x, end_y)


def print_star():
    for i in range(n):
        print(*star[i], sep='')


draw_star(1, 1, 1)
print_star()