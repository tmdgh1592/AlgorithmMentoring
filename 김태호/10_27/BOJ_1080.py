#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def switch(y, x):
    for i in range(3):
        for j in range(3):
            A[y + i][x + j] ^= 1

r, c = MIS()
res = 0
A = [list(map(int, input().rstrip())) for _ in range(r)]
B = [list(map(int, input().rstrip())) for _ in range(r)]

for i in range(r - 2):
    for j in range(c - 2):
        if A[i][j] != B[i][j]:
            switch(i, j)
            res += 1
            
print(res if A == B else -1)