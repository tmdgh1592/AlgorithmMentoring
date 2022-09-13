n = int(input())

lo = 0
hi = n

while lo <= hi:
    print(lo, hi)
    mid = (lo + hi) // 2
    if mid * mid < n:
        lo = mid + 1
    else:
        hi = mid - 1

print(lo)
print(11060446 ** 2)