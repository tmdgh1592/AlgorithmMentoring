#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = sorted(list(MIS()))

for i in range(1, n):
    data[i] += data[i - 1]

print(sum(data))