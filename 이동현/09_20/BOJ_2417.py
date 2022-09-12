import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

lo = 0
hi = n


while lo < hi:
    mid = (lo + hi) // 2

    if mid * mid < n:
        lo = mid + 1
    else:
        hi = mid - 1
print(lo)
