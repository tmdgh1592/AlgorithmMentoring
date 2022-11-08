import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n,m = MIS()
length = list(MIS())

lo = max(length)
hi = sum(length)

while lo <= hi:
    mid = (lo + hi) //2
    sum = 0
    cnt = 1
    for i in range(n):
        if sum + length[i] <= mid:
            sum += length[i]
        else:
            cnt += 1
            sum = length[i]
    if cnt > m: lo = mid + 1 #블루레이 크기 증가
    else: 
        hi = mid - 1 #블루레이 크기 감소
        res = mid

print(res)
