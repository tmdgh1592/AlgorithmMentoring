#질문;; 왜 틀리지?

import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, l = MIS()

rest = list(MIS())
rest.sort()
len_rest = len(rest)

lo = 1
hi = l - 1

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for i in range(n - 1):
        if rest[i + 1] - rest[i] > mid:
            cnt += (rest[i + 1] - rest[i] - 1)//mid 
    if cnt > m: #휴게소 설치를 더 많이 했으므로 거리를 늘림 
        lo = mid + 1
    else:#휴게소 설치를 조금 했으므로 거리를 줄임
        hi = mid - 1
print(mid)
