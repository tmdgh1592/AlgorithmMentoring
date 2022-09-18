# #
# import sys
# from collections import deque
# input = sys.stdin.readline
# MIS = lambda: map(int, input().rstrip().split())
# n = int(input())
# pb = []

# for _ in range(n):
#     dead, lamen = MIS()
#     pb.append((dead, lamen))

# pb.sort(key= lambda x:(x[0], -x[1]))
# # print(pb)

# q = deque()

# q.append(pb[0])
# deadline = pb[0][0]

# for i in range(1,n):
#     if deadline == pb[i][0]:
#         continue
#     else:
#         deadline = pb[i][0]

#     if len(q) < pb[i][0]:
#         q.appendleft(pb[i])

# sum = 0
# for i in list(q):
#     sum += i[1]
# print(sum)

import sys
import heapq
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
pb = []

for _ in range(n):
    dead, lamen = MIS()
    pb.append((dead, lamen))

pb.sort(key= lambda x:(x[0], x[1]))

rst = []

for deadline, lamen in pb:
    heapq.heappush(rst, lamen)
    if deadline < len(rst):
        heapq.heappop(rst)

print(sum(rst))
#힙 검색해서 안썻으면 절대 시간 안에 못풀거 같은데 ㅠ