#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
cnt = 1

for i in range(666, sys.maxsize):
    if str(i).find('666') != -1:
        if n == cnt:
            print(i)
            break
        cnt += 1
