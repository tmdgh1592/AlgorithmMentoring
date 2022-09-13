#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

s = input()

# 십진수 값 문자열 변환 -> 정수 변환 -> 합

for i in range(len(s)):

    cnt = list(str(ord(s[i])))
    cnt = sum(map(int, cnt))

    print(s[i] * cnt)
