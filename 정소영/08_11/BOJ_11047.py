#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
arr = list()
for _ in range(n):
    arr.append(int(input()))

res = 0
for i in range(n - 1, -1, -1):
    if k < arr[i]: continue
    
    res += k // arr[i]
    k %= arr[i]

print(res)