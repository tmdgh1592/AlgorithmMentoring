#-*- coding:utf-8 -*-
import sys
import heapq

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

left, right = list(), list()
res = list()

for _ in range(int(input())):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        tmp_left = heapq.heappop(left)
        tmp_right = heapq.heappop(right)
        heapq.heappush(right, -tmp_left)
        heapq.heappush(left, -tmp_right)
    
    res.append(-left[0])

print(*res,sep='\n')

