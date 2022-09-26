#-*- coding:utf-8 -*-
import sys
import heapq
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

data = sorted([list(MIS()) for _ in range(int(input()))], key=lambda x : (x[0], -x[1]))
res = []

for i in range(len(data)):
    if len(res) == data[i][0]:
        if res[0] < data[i][1]:
            heapq.heappop(res)
            heapq.heappush(res, data[i][1])
    else:
        heapq.heappush(res, data[i][1])

print(sum(res))