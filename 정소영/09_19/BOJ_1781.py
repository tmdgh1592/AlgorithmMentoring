#-*- coding:utf-8 -*-
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

data = sorted([list(MIS()) for _ in range(n)],key=lambda x: x[0])

res = []

for deadline, cnt in data:
    heapq.heappush(res, cnt)
    if len(res) > deadline:
        heapq.heappop(res)
print(sum(res))
