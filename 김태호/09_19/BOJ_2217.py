#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

data = sorted([int(input()) for _ in range(int(input()))], reverse=True)

for i in range(len(data)):
    data[i] *= i + 1
print(max(data))