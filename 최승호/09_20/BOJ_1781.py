# -*- coding:utf-8 -*-
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def MIS(): return map(int, input().rstrip().split())


result = []
q = []

for _ in range(int(input())):
    deadline, count = MIS()
    heapq.heappush(q, (deadline, count))

while q:
    deadline, ramen = heapq.heappop(q)
    heapq.heappush(result, ramen)

    if deadline < len(result):
        heapq.heappop(result)

print(sum(result))