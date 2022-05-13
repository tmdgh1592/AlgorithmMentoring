#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS() 

def recursion(lst, here):
    if len(lst) == m:
        print(*lst)
        return None
    
    for there in range(here, n + 1):
        # if there not in lst:
        lst.append(there)
        recursion(lst, there)
        lst.pop()

recursion(list(), 1)