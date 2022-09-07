#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list()
for _ in range(n):
    start, end = MIS()
    arr.append((start, end))

# 끝나는 시간 정렬 후 시작시간으로 정렬
arr = sorted(arr, key= lambda x: x[0])
arr = sorted(arr, key= lambda x: x[1])

temp = 0
cnt = 0

for start, end in arr:
    if start >= temp:
        cnt += 1
        temp = end

print(cnt)

