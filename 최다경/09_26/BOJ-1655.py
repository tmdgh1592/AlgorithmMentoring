import sys, heapq
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
min_h = []
max_h = []
res = []
n = int(input())
for i in range(n):
    num = int(input())
    if len(min_h) == len(max_h):
        heapq.heappush(max_h, num * -1)
    else:
        heapq.heappush(min_h, num)
    if len(min_h) > 0 and max_h[0] * -1 > min_h[0]:
        mi = heapq.heappop(max_h)
        ma = heapq.heappop(min_h)
        heapq.heappush(min_h, ma)
        heapq.heappush(max_h, mi * -1)
    res.append(max_h[0] * -1)
for i in res:
    print(i)