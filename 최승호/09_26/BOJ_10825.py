#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [tuple(input().rstrip().split()) for _ in range(n)]
arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for info in arr: print(info[0])