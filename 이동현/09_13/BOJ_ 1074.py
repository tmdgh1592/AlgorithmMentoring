import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, r, c = MIS()


cnt = 0


while n != 0:
    n -= 1
    if r < (2 ** n) and c < (2 ** n):
        cnt += 0

    elif r < (2 ** n) and c >= (2 ** n):
        cnt += (2 ** n) * (2 ** n)
        c -= (2 ** n)

    elif r >= (2 ** n) and c < (2 ** n):
        cnt += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
        
    else:
        cnt += (2 ** n) * (2 ** n) * 3
        c -= (2 ** n)
        r -= (2 ** n)

print(cnt)