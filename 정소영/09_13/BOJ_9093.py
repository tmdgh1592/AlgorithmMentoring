#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    arr = list(input().rstrip().split())
    res = list()
    for word in arr:
        res.append(word[::-1])
    print(*res)