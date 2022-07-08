#-*- coding:utf-8 -*-
from itertools import permutations
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

def f(arr):
    global n

    if len(arr) == n:
        print(*arr)
        return None
    
    for i in range(1, n + 1):
        if i in arr: continue;
        arr.append(i)
        f(arr)
        arr.pop()
        
f(list())