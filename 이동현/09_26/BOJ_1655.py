import sys
import heapq
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

left = list()
right =list()

n = int(input())

for i in range(n):
    number = int(input())
    if len(left) <= len(right):
        heapq.heappush(left, -number) #left is maxheap
    else:
        heapq.heappush(right,number) #right is minheap
    
    if right and left[0] > right[0]:
        temp1 = heapq.heappop(left)
        temp2 = heapq.heappop(right)
        heapq.heappush(left, -temp2)
        heapq.heappush(right, -temp1)
    print(-left[0])
