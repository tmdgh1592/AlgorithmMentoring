import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, l = MIS()
lo = 1
hi = l - 1
rest = list(MIS())
rest.append(0)
rest.append(l)
rest.sort()


res = 0

while lo <= hi:
    cnt = 0
    mid = (lo + hi) // 2
    for i in range(len(rest) - 1):
        length = rest[i + 1] - rest[i]
        if length > mid:
            cnt += (length - 1) // mid
    if cnt > m: #거리를 늘린다.
        lo = mid + 1
    else: #거리를 줄인다.
        res = mid
        hi = mid - 1

print(res)