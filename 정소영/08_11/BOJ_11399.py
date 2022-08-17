#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
p = sorted(list(MIS()))
res = 0
ans = []
for i in range(n):
    res += p[i]
    ans.append(res)

print(sum(ans))