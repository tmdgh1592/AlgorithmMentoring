#-*- coding:utf-8 -*-
import heapq
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

# min heap은 중간값보다 큼
# max heap은 중간값보다 작음
min_q, max_q = [], []

for _ in range(n):
    val = int(input())

    if len(min_q) == len(max_q): heapq.heappush(max_q, -val)
    else: heapq.heappush(min_q, val)

    # max heap의 root가 더 크면 스왑
    if min_q and min_q[0] < -max_q[0]:
        min_root = -heapq.heappop(min_q)
        max_root = -heapq.heappop(max_q)

        heapq.heappush(max_q, min_root)
        heapq.heappush(min_q, max_root)
    
    print(-max_q[0])