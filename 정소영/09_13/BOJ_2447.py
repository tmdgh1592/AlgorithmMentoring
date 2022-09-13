#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [[' ' for _ in range(2500)] for _ in range(2500)]
y, x = 0 , 0

box_size = 3

def base(y, x):
    for i in range(box_size):
        for j in range(box_size):
            if i == 1 and j == 1:
                continue
            else:
                arr[y + i][x + j] = '*'

def recursive(y, x, box_size):
    if box_size == 3:
        base(y, x)
        return
    
    next_box_size = box_size // 3

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                recursive(y + i * next_box_size, x + j * next_box_size, next_box_size)

recursive(y, x, n)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end='')
    print()
