# import sys

# input = sys.stdin.readline
# MIS = lambda: map(int, input().rstrip().split())
# n = int(input())
# data = [0 for _ in range(n)]

# for i in range(n):
#     d, r = MIS()
#     data[i] = [d, r]

# data = sorted(data, key = lambda x : x[0])
# su = 0
# for i in range(1, n):
#     ma = 0
#     for j in range(i - 1, n):
#         if data[j][0] == i:
#             ma = max(ma, data[j][1])
#     su += ma

# print(su) 

import sys, heapq
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

hq = []
result = []

for i in range(int(input())):
    dl, cnt = MIS()
    heapq.heappush(hq, (dl, cnt))

while hq:
    dl, cnt = heapq.heappop(hq)
    heapq.heappush(result, cnt)
    if dl < len(result):
        heapq.heappop(result)

print(sum(result))
print(result)
