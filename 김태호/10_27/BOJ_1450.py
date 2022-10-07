#-*- coding:utf-8 -*-
from bisect import bisect_right
import sys
from itertools import combinations
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, c = MIS()
data = list(MIS())
left, right = list(), list()

res = 0
half = len(data) // 2

for i in range(half + 1):
    left += list(map(sum, combinations(data[:half], i)))

for i in range(n - half + 1):
    right += list(map(sum, combinations(data[half:], i)))

right = sorted(right)

for e in left:
    res += bisect_right(right, c - e)

print(res)