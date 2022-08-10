#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
data = list()
cnt = 0

for _ in range(n):
    data.append(int(input()))
    
for i in range(n - 1, -1, -1):
    cnt += k // data[i]
    k %= data[i]
print(cnt)