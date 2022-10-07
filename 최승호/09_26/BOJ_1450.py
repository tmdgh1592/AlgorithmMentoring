#-*- coding:utf-8 -*-
from bisect import bisect_right
from itertools import combinations
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, c = MIS()
arr = list(MIS())
res, half = 0, n // 2
left, right = arr[:half], arr[half:]
left_sum, right_sum = [], []

for i in range(half + 1): left_sum += list(map(sum, combinations(left, i)))
for i in range(n - half + 1): right_sum += list(map(sum, combinations(right, i)))
left_sum.sort()

for val in right_sum: res += bisect_right(left_sum, c - val)

print(res)