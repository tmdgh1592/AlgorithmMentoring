#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = [list(MIS()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return (y >= 0 and y < n ) and (x >= 0 and x < m)

# 빙산 위치 확인, 빙산이 녹고 없어진 자리도 영향을 줌