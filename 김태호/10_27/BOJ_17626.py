#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
cache = [float('inf') for _ in range(50001)]
cache[0] = 0
cache[1] = 1
for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        cache[i] = min(cache[i - j * j] + 1, cache[i])
        j += 1

print(cache[n])
