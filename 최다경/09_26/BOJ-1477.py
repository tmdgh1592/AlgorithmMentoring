import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n, m, l = MIS()
data = sorted(MIS())
data.sort
data.insert(0, 0)
data.append(l)

s, e = 1, l - 1
res = 0
while(s <= e):
    cnt = 0
    mi = (s + e) // 2
    for i in range(1, len(data)):
        if data[i] - data[i - 1] > mi:
            cnt += (data[i] - data[i - 1] - 1) // mi
        
    if cnt > m:
        s = mi + 1
    else:
        e = mi - 1
        res = mi

print(res)

