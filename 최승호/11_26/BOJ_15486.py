#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = [[0, 0]] + [list(MIS()) for _ in range(n)]
cache = [0] * (n + 2)

for days in range(1, n + 1):
    cache[days] = max(cache[days], cache[days - 1])
    
    spent, money = data[days]
    if days + spent <= n + 1:
        cache[days + spent] = max(cache[days + spent], cache[days] + money)

print(max(cache))