#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = float('inf')

n = int(input())
cache = [INF] * (n + 1) # x를 1로 만드는 최소 연산 횟수
cache_string = ['1'] * (n + 1)
cache[1] = 0

for i in range(2, n + 1):
    if cache[i] > cache[i - 1] + 1:
        cache[i] = cache[i - 1] + 1
        cache_string[i] = str(i) + ' ' + cache_string[i - 1]
    if i % 3 == 0 and cache[i] > cache[i // 3] + 1:
        cache[i] = cache[i // 3] + 1
        cache_string[i] = str(i) + ' ' + cache_string[i // 3]
    if i % 2 == 0 and cache[i] > cache[i // 2] + 1:
        cache[i] = cache[i // 2] + 1
        cache_string[i] = str(i) + ' ' + cache_string[i // 2]

print(cache[n], cache_string[n], sep='\n')