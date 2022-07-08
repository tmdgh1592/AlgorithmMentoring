#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())

for i in range(n-1,0,-1):
    if arr[i-1] < arr[i]:
        for j in range(n-1,0,-1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                break
        print(*arr)
        exit()

print(-1)
