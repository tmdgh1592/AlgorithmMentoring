import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
lo, hi = 1, arr[-1]

def is_installable(dist):
    prev, cnt = 0, 1

    for i in range(1, len(arr)):
        if (arr[i] - arr[prev]) >= dist:
            cnt+=1; prev = i
        if cnt == c:
            return True

    return False


while lo <= hi:
    mid = (lo + hi) // 2

    if is_installable(mid):
        lo = mid+1
    else:
        hi = mid-1
    
print(hi)