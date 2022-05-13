#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
SIZE = 2500

arr = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def base_save_star(y, x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                arr[y + i][x + j] = '*'

def recursion(y, x, box_size):
    if box_size == 3:
        base_save_star(y, x)
        return None
    
    next_box_size = box_size // 3
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                recursion(y + i * next_box_size, x + j * next_box_size, next_box_size)

def solve():
    recursion(0, 0, n)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='')
        print()

solve()