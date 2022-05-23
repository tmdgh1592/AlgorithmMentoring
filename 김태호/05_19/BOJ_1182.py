#-*- coding:utf-8 -*-
import sys
from itertools import combinations


sys.setrecursionlimit(1 << 18)


sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = list(MIS())
res = 0

# def f(idx, cur_sum):
#     global res
    
#     if idx == n:
#         return None
    
#     if cur_sum + arr[idx] == m:
#         res += 1
    
#     f(idx + 1, cur_sum + arr[idx])
#     f(idx + 1, cur_sum)
    
# f(0, 0)
# print(res)

for i in range(1, n + 1):
    for perm in combinations(arr, i):
        if sum(perm) == m:
            res += 1
            
print(res)