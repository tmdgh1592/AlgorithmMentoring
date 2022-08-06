#-*- coding:utf-8 -*-
import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

num = 666
cnt = 0

while True:
    if '666' in str(num):
        cnt += 1
        if n == cnt:
            break
    num += 1

print(num)
