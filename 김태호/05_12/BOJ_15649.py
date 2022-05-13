#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()

def recursion(lst):
    if len(lst) == m:
        print(*lst)
        return None
    
    for here in range(1, n + 1):
        if here not in lst:
            lst.append(here)
            recursion(lst)
            lst.pop()

recursion(list())