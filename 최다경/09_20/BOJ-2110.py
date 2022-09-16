n, c = map(int, input().rstrip().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr)

lo = 1
hi = arr[-1] - arr[0]

def is_possible(dist):
    cnt = c - 1
    pos = arr[0]
    for i in range(1, n):
        if pos + dist <= arr[i]:
            pos = arr[i]
            cnt -= 1
        if cnt <= 0:
            return True
    else:
        return False

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)
#시간 초과
