import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
N, r, c = map(int, input().rstrip().split())
cnt = 0

def visit(x, y, n, t):
    global cnt

    if n == 0:
        if x == r and y == c:
            print(cnt)
            exit(0)
        cnt += 1
        return

    if not (x <= r < x+t and y <= c < y+t):
        cnt += (t**2)
        return

    visit(x, y, int(n / 2), t // 2)
    visit(x, y+n, int(n / 2), t// 2)
    visit(x+n, y, int(n / 2), t// 2)
    visit(x+n, y+n, int(n / 2), t // 2)

visit(0, 0, 2**(N-1), 2 ** N)
