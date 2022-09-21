#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 14)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(s, e):
    if s >= e: return 1
    if cache[s][e] != -1: return cache[s][e]

    if data[s] == data[e]:
        cache[s][e] = f(s + 1, e - 1)
        return cache[s][e]
    return 0

n = int(input())
data = list(MIS())
cache = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    cache[i][i] = True

for _ in range(int(input())):
    lo, hi = map(lambda x : x - 1, MIS())
    print(f(lo, hi))
